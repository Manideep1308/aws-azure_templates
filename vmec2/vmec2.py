from flask import Flask, request
from flask_cors import CORS
 
 
app = Flask(__name__)
CORS(app) 
 
@app.route('/vm', methods=['POST'])

def fun():

    cloudenv = request.args.get('cloudenv')
    instancename = request.args.get('instancename')
    instancetype = request.args.get('instancetype')
    instancevolume = request.args.get('instancevolume')                          
    authenticationType = request.args.get('authenticationType')
    nicname = request.args.get('nicname')
    stacknumber = request.args.get('stacknumber')   
    vpcname = request.args.get('vpcname')
    securitygroupname = request.args.get('securitygroupname')  
    keyname = request.args.get('keyname')


   
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

'    "vmName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(instancename) + '",\n'
'      "metadata": {\n'
'        "description": "The name of you Virtual Machine."\n'
'      }\n'
'    },\n'
'    "adminUsername": {\n'
'      "type": "string",\n'
'      "defaultValue": "testuser",\n'
'      "metadata": {\n'
'        "description": "Username for the Virtual Machine."\n'
'      }\n'
'    },\n'
'    "authenticationType": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(authenticationType) + '",\n'
'      "allowedValues": [\n'
'        "sshPublicKey",\n'
'        "password"\n'
'      ],\n'
'      "metadata": {\n'
'        "description": "Type of authentication to use on the Virtual Machine. SSH key is recommended."\n'
'      }\n'
'    },\n'
'    "adminPasswordOrKey": {\n'
'      "type": "secureString",\n'
'      "defaultValue": "Open2022$",\n'
'      "metadata": {\n'
'        "description": "SSH Key or password for the Virtual Machine. SSH key is recommended."\n'
'      }\n'
'    },\n'

'    "ubuntuOSVersion": {\n'
'      "type": "string",\n'
'      "defaultValue": "18.04-LTS",\n'
'      "allowedValues": [\n'
'        "12.04.5-LTS",\n'
'        "14.04.5-LTS",\n'
'        "16.04.0-LTS",\n'
'        "18.04-LTS",\n'
'        "20.04-LTS"\n'
'      ],\n'
'      "metadata": {\n'
'        "description": "The Ubuntu version for the VM. This will pick a fully patched image of this given Ubuntu version."\n'
'      }\n'
'    },\n'  
'    "vmSize": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(instancetype) + '",\n'
'      "metadata": {\n'
'        "description": "The size of the VM"\n'
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
'    "variables": {\n'

'     "networkInterfaceName": "' + str(nicname) + '",\n'
'    "osDiskType": "' + str(instancevolume) + '",\n'
'    "linuxConfiguration": {\n'
'      "disablePasswordAuthentication": true,\n'
'      "ssh": {\n'
'        "publicKeys": [\n'
'          {\n'
'            "path": "[format(''\'/home/{0}/.ssh/authorized_keys\', parameters(''\'adminUsername\'''))]",\n'
'            "keyData": "[parameters(''\'adminPasswordOrKey\''')]"\n'
'          }\n'
'        ]\n'
'      }\n'
'    }\n'
'  },\n'
'    "resources": [\n'

'        {\n'
'      "type": "Microsoft.Compute/virtualMachines",\n'      #virtualmachine
'      "apiVersion": "2021-11-01",\n'
'      "name": "[parameters(''\'vmName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "hardwareProfile": {\n'
'          "vmSize": "[parameters(''\'vmSize\''')]"\n'
'        },\n'
'        "storageProfile": {\n'
'          "osDisk": {\n'
'            "createOption": "FromImage",\n'
'            "managedDisk": {\n'
'              "storageAccountType": "[variables(''\'osDiskType\''')]"\n'
'            }\n'
'          },\n'
'          "imageReference": {\n'
'            "publisher": "Canonical",\n'
'            "offer": "UbuntuServer",\n'
'            "sku": "[parameters(''\'ubuntuOSVersion\''')]",\n'
'            "version": "latest"\n'
'          }\n'
'        },\n'
'         "networkProfile": {\n'
'          "networkInterfaces": [\n'
'            {\n'
'              "id": "[resourceId(''\'Microsoft.Network/networkInterfaces\', variables(''\'networkInterfaceName\'''))]"\n'
'            }\n'
'          ]\n'
'        },\n'
'        "osProfile": {\n'
'          "computerName": "[parameters(''\'vmName\''')]",\n'
'          "adminUsername": "[parameters(''\'adminUsername\''')]",\n'
'          "adminPassword": "[parameters(''\'adminPasswordOrKey\''')]",\n'
'          "linuxConfiguration": "[if(equals(parameters(''\'authenticationType\'''), ''\'password\'''), null(), variables(''\'linuxConfiguration\'''))]"\n'
'        }\n'
'       }\n'        
'      }\n'
'  ]\n'
'}\n'
 )

    data2=(

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
'        sec_group1 =ec2.SecurityGroup.from_lookup_by_name(self, "iac_sg1", vpc=vpc, security_group_name="' + str(securitygroupname) + '")\n'
        
                
'        # Instance Role and SSM Managed Policy\n'
'        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))\n'
'        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))\n'


'        # ubuntu image\n'
'        ub_image = ec2.MachineImage.from_ssm_parameter("/aws/service/canonical/ubuntu/server/focal/stable/current/amd64/hvm/ebs-gp2/ami-id")\n'

'        # Instance1\n'
'        instance = ec2.Instance(self, "IaCInstance1", instance_name="' + str(instancename) + '",\n'
'            instance_type=ec2.InstanceType("' + str(instancetype) + '"),\n'
'            machine_image=ub_image,\n'
'            block_devices=[\n'
'                ec2.BlockDevice(device_name="/dev/sda1", volume=ec2.BlockDeviceVolume.ebs(' + str(instancevolume) + '))\n'
'            ],\n'
'            vpc = vpc,\n'            
'            vpc_subnets=ec2.SubnetSelection(\n'
'                subnet_type=ec2.SubnetType.PUBLIC\n'
'             ),\n'
'            role=role,\n'
'            security_group=sec_group1,\n'
'            key_name = "' + str(keyname) + '"\n'
'            )\n'
    


    )
   


    if(str(cloudenv) =='aws'):
     with open('ec2_template.py', 'w') as f:
        print(data2, file=f)

     return (
            '{\n'
            '        "stacknumber": "' + str(stacknumber) + '",\n'
            '        "vpcname": "' + str(vpcname) + '",\n'
            '        "securitygroupname": "' + str(securitygroupname) + '",\n'
            '        "instancename": "' + str(instancename) + '",\n'
            '        "instancetype": "' + str(instancetype) + '",\n'
            '        "authenticationType": "' + str(authenticationType) + '",\n'
            '        "instancevolume": "' + str(instancevolume) + '",\n'
            '        "nicname": "' + str(nicname) + '",\n'
            '        "keyname": "' + str(keyname) + '",\n'
            '        "cloudenv": "' + str(cloudenv) + '"\n'

            '}\n'
        )

         

    if(str(cloudenv) =='azure'):
     with open('vmnetworkinterface_template.json','w') as f:
        print(data1, file=f)
 

     return data1

app.run(port=1005, host='0.0.0.0',debug=True)      