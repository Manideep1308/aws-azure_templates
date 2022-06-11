from flask import Flask, request
from flask_cors import CORS
 
 
app = Flask(__name__)
CORS(app) 
 
@app.route('/nic', methods=['POST'])

def fun():
    vpcname = request.args.get('vpcname')
    securitygroupname = request.args.get('securitygroupname')
    subnetname = request.args.get('subnetname')
    publicIpname = request.args.get('publicIpname')
    nicname = request.args.get('nicname')

    data = (
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
'      "vnetName": {\n'
'        "type": "string",\n'
'        "defaultValue": "'+ str(vpcname)+ '",\n'
'        "metadata": {\n'
'          "description": "VNet name"\n'
'        }\n'
'      },\n'
'      "subnetName": {\n'
'        "type": "string",\n'
'        "defaultValue": "' + str(subnetname) + '",\n'
'        "metadata": {\n'
'          "description": "Subnet 1 Name"\n'
'        }\n'
'      },\n'
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
'    "variables": {\n'
'    "publicIPAddressName": "' + str(publicIpname) + '",\n'
'     "networkInterfaceName": "' + str(nicname) + '"\n'
'     },\n'
'    "resources": [\n'
'        {\n'
'      "type": "Microsoft.Network/networkInterfaces",\n'
'      "apiVersion": "2016-06-01",\n'
'      "name": "[variables(''\'networkInterfaceName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "ipConfigurations": [\n'
'          {\n'
'            "name": "ipconfig1",\n'
'            "properties": {\n'
'              "subnet": {\n'
'                "id": "[resourceId(''\'Microsoft.Network/virtualNetworks/subnets\', parameters(''\'vnetName\'''), parameters(''\'subnetName\'''))]"\n'
'              },\n'
'              "privateIPAllocationMethod": "Dynamic",\n'
'              "publicIPAddress": {\n'
'                "id": "[resourceId(''\'Microsoft.Network/publicIPAddresses\', variables(''\'publicIPAddressName\'''))]"\n'
'             }\n'
'            }\n'
'          }\n'
'        ],\n'
'        "networkSecurityGroup": {\n'
'          "id": "[resourceId(''\'Microsoft.Network/networkSecurityGroups\', parameters(''\'networkSecurityGroupName\'''))]"\n'
'        }\n'
'      }\n'
'    }\n'
'  ]\n'
'}\n'
    )


    with open('nic_template.json','w') as f:
      print(data, file=f)


    return data


app.run(port=1004, host='0.0.0.0')    