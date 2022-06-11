
from flask import Flask, request
from flask_cors import CORS
 
 
app = Flask(__name__)
CORS(app) 
 
@app.route('/secgroup', methods=['POST'])

def fun():
  cloudenv = request.args.get('cloudenv') 
  securitygroupname = request.args.get('securitygroupname') 
  rulename = request.args.get('rulename')          
  protocol = request.args.get('protocol')
  priority = request.args.get('priority')
  direction = request.args.get('direction')
  ipaddress = request.args.get('ipaddress')
  port = request.args.get('port')
  stacknumber = request.args.get('stacknumber')                       
  vpcname = request.args.get('vpcname')
  
  



  data1 = (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n'
'    "parameters": {\n'
'      "networkSecurityGroupName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(securitygroupname) + '",\n'
'      "metadata": {\n'
'        "description": "Name of the Network Security Group"\n'
'      }\n'
'    },\n'
'    "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'
'    "resources": [\n'
'      {\n'
'      "type": "Microsoft.Network/networkSecurityGroups",\n'
'      "apiVersion": "2016-06-01",\n'
'      "name": "[parameters(''\'networkSecurityGroupName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "securityRules": [\n'
'          {\n'
'            "name": "' + str(rulename) + '",\n'
'            "properties": {\n'
'              "priority": ' + str(priority) + ',\n'
'            "protocol": "' + str(protocol) + '",\n'
'              "access": "Allow",\n'
'              "direction": "' + str(direction) + '",\n'
'              "sourceAddressPrefix": "' + str(ipaddress) + '",\n'
'              "sourcePortRange": "*",\n'
'              "destinationAddressPrefix": "*",\n'
'              "destinationPortRange": "' + str(port) + '"\n'
'            }\n'
'          }\n'
'        ]\n'
'      }\n'
'    }\n'
'  ]\n'
'}\n'
  )

  data2 = (

'from aws_cdk import (\n'
'    aws_ec2 as ec2, aws_iam as iam, Stack\n'

')\n'

'from constructs import Construct\n'

'\n'
'class CdkEc2Stack' + str(stacknumber) + '(Stack):\n'
'\n'
'    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:\n'
'        super().__init__(scope, construct_id,  **kwargs)\n'
'\n'
'        vpc = ec2.Vpc.from_lookup(self, "MyVpc", vpc_name="' + str(vpcname) + '")\n'
'\n'
'        sec_group1 = ec2.SecurityGroup(self, "iac_sg1",\n'
'            vpc=vpc, security_group_name="' + str(securitygroupname) + '",\n'
'           allow_all_outbound=True,\n'
'            )\n'
        
'      # add a new ingress rule to allow port 22 to internal hosts\n'
'        sec_group1.add_ingress_rule(\n'
'            peer=ec2.Peer.ipv4("' + str(ipaddress) + '"),\n'
'            description="Allow SSH connection", \n'
'            connection=ec2.Port.' + str(protocol) + '(' + str(port) + ')\n'
'            )'


    )
  
  if(str(cloudenv) =='aws'):
   with open('sec_template.py', 'w') as f:
        print(data2, file=f)

   return (
            '{\n'
            '        "stacknumber": "' + str(stacknumber) + '",\n'
            '        "vpcname": "' + str(vpcname) + '",\n'
            '        "securitygroupname": "' + str(securitygroupname) + '",\n'
            '        "rulename": "' + str(rulename) + '",\n'
            '        "protocol": "' + str(protocol) + '",\n'
            '        "priority": "' + str(priority) + '",\n'
            '        "direction": "' + str(direction) + '",\n'
            '        "port": "' + str(port) + '",\n'
            '        "ipaddress": "' + str(ipaddress) + '",\n'
            '        "cloudenv": "' + str(cloudenv) + '"\n'

            '}\n'
        )


  if(str(cloudenv) =='azure'):
   with open('secgroup_template.json','w') as f:
      print(data1, file=f)


   return data1


app.run(port=1002, host='0.0.0.0')    