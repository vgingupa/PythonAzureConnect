from os import environ as env
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from azure.mgmt.compute import ComputeManagementClient


#AZURE_CLIENT_ID="528c082f-4bfd-4941-ae6e-66b59a78c920"
#AZURE_CLIENT_SECRET="dZF1d~BUVI.cnHQGw58fw8pFevfR~e19YI"
#AZURE_SUBSCRIPTION_ID="0266d00b-f7f1-40cd-b895-35e76be40442"
#AZURE_TENANT_ID="2b65c7f1-1021-4303-8c3c-3e0392c68a96"
#KEYVAULT_NAME="Pythonkeyvalut"
AZURE_CLIENT_ID=env.get("AZURE_CLIENT_ID", "")
AZURE_CLIENT_SECRET=env.get("AZURE_CLIENT_SECRET", "")
AZURE_SUBSCRIPTION_ID=env.get("AZURE_SUBSCRIPTION_ID", "")
AZURE_TENANT_ID=env.get("AZURE_TENANT_ID", "")
KEYVAULT_NAME=env.get("AZURE_KEYVAULT_NAME", "")
KEYVAULT_URL=f'https://{KEYVAULT_NAME}.vault.azure.net'


_credential = ClientSecretCredential(
    tenant_id=AZURE_TENANT_ID,
    client_id=AZURE_CLIENT_ID,
    client_secret=AZURE_CLIENT_SECRET   
)

_sc = SecretClient(vault_url=KEYVAULT_URL, credential=_credential)
testvalue=_sc.get_secret("test").value
print(testvalue)




compute_client = ComputeManagementClient(_credential,AZURE_SUBSCRIPTION_ID)

#vm_list = compute_client.virtual_machines.list_all()
vm_list = compute_client.virtual_machines.get(resource_group_name="LinuxVM",vm_name="LinuxVM",expand='instanceView')
#filtered = [vm for vm in vm_list if vm.name == "LinuxVM"] #All VMs that match

#vm = filtered[0] #First VM

#print(f"vm size: {vm.hardware_profile.vm_size}")  
#print(f'vm name is {vm.name}')
print(vm_list.vm_id)



