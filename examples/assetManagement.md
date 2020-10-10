# Asset Management Examples
Here are some examples listed how an asset management might work with simple tools.
## Asset management with git
All templates can be used and stored in git to have a searchable documentation base.  


## Azure Tenant security contacts and subscriptions
This script crawls all subscription where the logged in account has access to.
```
from azure.common.client_factory import get_client_from_cli_profile
from azure.common.credentials import get_cli_profile
from azure.mgmt.security import SecurityCenter
from azure.mgmt.resource import SubscriptionClient, ResourceManagementClient

sub_client = get_client_from_cli_profile(SubscriptionClient)

o = {}

for sub in sub_client.subscriptions.list():
    o[sub.subscription_id] = {'name': sub.display_name, 'contacts':[], 'error': None }
    try:
        contact_client = get_client_from_cli_profile(SecurityCenter, subscription_id=sub.subscription_id, asc_location='')
        for contact in contact_client.security_contacts.list():
            o[sub.subscription_id]['contacts'].append({ 'type': contact.type, 'name': contact.name, 'email': contact.email, 'phone': contact.phone})
    except Exception as e:
         o[sub.subscription_id]['error'] = repr(e)

print(o)
```