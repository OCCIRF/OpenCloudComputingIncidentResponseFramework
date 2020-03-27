# Incident preparation
The preparation is an integral part of the incident response process. Here you need to plan and prepare your strategy
and your tools.

{:toc}

## Asset management
To properly react to an incident in the own environment an asset management needs to be established. The asset
management contains all relevant assets which might be helpful in an incident case. Those assets are (not all):
- Accounts or Subscriptions (Public Cloud/SaaS)
- Running services
  - IP addresses
  - Servers / components (like databases, application server services)
  - Service owners
  - Criticality
  - Processed data
- ***@TODO: More needed***

Those fact sheets can be stored in an asset management tool or a simple database (See
[examples/assetManagement](../examples/assetManagement.md)). Also, an offline version is possible as in an incident case
it is not guaranteed that the online asset management tools are accessible (See
[templates/assetFactsSheet](../templates/assetFactsSheet.md)).  
The more precisely the facts sheets are the easier it is to get all needed assets in an incident case. To assure that
all facts sheets are up to date a periodic review should be done.
   
## Roles and responsibilities
Defined responsibilities are important in an incident process as all involved persons need to know what they need to do.
The employees within the set responsibilities should be skilled to handle those in a pressure situation like an incident
event. The roles and responsibilities should also be documented. An example document can be found
[here](../templates/rolesAndResponsibilities.md).

### Incident Response Team
#### On-call team
The on-call security team is the main contact and initial responder to all suspected security events. They should be
staffed for 24/7. They are responsible for evaluating incoming events and classify them accordingly. The on-call team is
notifying the incident investigators to handle the incident, if one is detected. 

#### Incident Investigators
The incident investigators are collection and analysing evidence of the incident. They try to find the root cause if the
incident and will implement short-term mitigation measures. The lead investigator is controlling the actions of the
investigations team and direct the tasks of them.

#### Incident Manager
The incident manager responsible for handling the incident on the non-technical side. He is controlling the processes
and is deciding together with the lead investigator the next steps. He is also coordinating the response activities and
keeps the team focused on the incident. To help the team he can refer to other departments like the service teams or the
upper management.

#### Communication Manager
The communication manager is handling all sorts of communication to other parties who are involved in the incident. He
writes press releases or notifications to customers if they are affected. Also, an important communication partner are
the law enforcements as legal responsibilities are needed to be followed (Like GDPR or KRITIS in Germany). He is
responsible for internal communications, too. E.g. communicating the comments on the incident and the affected systems
to the internal employees.

#### Trainers
It is very important to train the different departments regarding incident response and general security. If there is no
ongoing incident the team members of the incident response team should train the colleagues to improve the security
knowledge. The trainers are not relevant for an incident, but they are helping a lot to prevent those.

### Other internal departments
#### Legal Manager
The legal manager is responsible for legal questions for the incident. He as to provide contact details to authorities
to the communication manager or work with him together on statements for them. He can also consult the management, or
the incident response team in legal questions.Moreover, he needs also help the team in GDPR topics if there is no
dedicated department for data protection in the organisation.

#### IT operations
Normally the IT operations are responsible for the deployed solutions. In an incident case they have the most knowledge
about their infrastructure. The incident response team should be able to get in touch with those operation teams if they
can help resolve the incident. Those contacts need to be stated in the asset facts sheet, so a contact person is always
known. (@TODO: Azure list security contacts)

### Providers
As all cloud solutions are based on a provider it is important to have a direct line of contact to them. For that case a
single point of contact is important. This contact is always reachable and can support the incident response operations.
The single point of contact can be a support team or the Security Operations Center (SOC). This point of contacts should
be regularly reviewed and tested.

### Customers
It is also important to notify the customers in case of an incident where the data of those customers are affected. This
needs also be planned accordingly to be satisfy legal requirements and corporate policies. A list of customers should be
easily accessible to inform potential affected customers.

## Access concept
The access concept for incident response is an interesting topic. Here it is important to guarantee quick reaction times
but also honor the least privileges principle. Here the CSIRT needs to balance the least privileges concept and the
possibility to quickly access any affected systems.

### Normal access
While normal operating the CSIRT needs access to the project accounts/subscriptions only as read-only users. Read-only
access is necessary to get log data or metrics to a central log environment. The best way to guarantee the read-only
access is to force this via an identity management system (Like the Azure AD or AWSs IAM). This identity management
system forces the CSIRT group into all corporate subscriptions/accounts. ***@TODO: Add link to log preparation***

![Normal access to a subscription / account](accessConceptDefault.png)

### Emergency access
When an incident is occurring in the environment the incident response team needs to access the environment quickly to
contain the incident. As the CSIRT cannot have full access to all environment at all time a 3rd party needs to grant the
elevated access. This 3rd party as a trusted source helps to guarantee a four-eyes principle and that the principle of
least privileges his honoured. A workflow for this access could look like following:
1. The CSIRT team members requests the privileges at the trusted party
2. This trusted party logs into the IdM system and grants the specific users full access to the requested environment
3. The CSIRT team members can now authenticate with their normal users at the IdM to get the higher privileges
4. The team has full access into the infected environment

There are different possibilities to define the role of the trusted party to grant the CSIRT members access to the
infected environment. The first possibility is that the contact is an admin from the IdM admin team which is also
on-call. The second option is that a manager on duty or someone from the operations team for this environment can handle
those access rights and give them to the team. A third and possible fasted way to handle the emergency access is a
breaking-glass account which is handled by the manager on duty of the CSIRT. A breaking-glass account is an account
which is only there for emergency access and is able to delegate specific access roles to a set of users. In this
scenario the incident handler is requesting access from his manager. The manager then uses this special account in the
identity manager to grant the incident handler access to the subscription. All those administrative actions have to be
of course be logged and alerted. Also, a timeline needs to be specified for the validity of the accounts. So they can be
removed when they are no longer needed.
A template for the emergency access can be found [here](../templates/emergencyAccess.md).

![Emergency access to a subscription / account](accessConceptIncident.png)

## Communication
The communication of the incident is also very important. Especially when someone outside of the organisation has to be
informed about an incident. The communication should always be done by the communication manager or a trained
communication employee if possible. The communication is key for the reputation of the affected organisation. Also, it
is important to communicate clear and through defined channels. Which is also in responsibility of the communication
manager.  
Communication examples can be found [here](../examples/communication.md).

### Communication to the cloud provider
The communication to the cloud provider is needed when an incident is reported by the cloud provider or is also
affecting their systems. Here a more technical communication should be preferred between both CSIRTs. The communication
needs to be clarified when the shared responsibility is defined in the contracts. This can also be done in the UI of the
Cloud providers like Azure does it with the security contacts.

### Internal communication
Internal communication is important to inform the employees about incidents generally. When some employees are affected
they also should be separately notified to guarantee the security of those employees. Also, when the incident is closed
the whole company can be informed about that to lean what can be improved (lessons learned). If the CSIRT needs help
from different teams a communication channel to those also needs to be established via the communications manager or
directly via the line managers.

### Communication to customers


### Communication to law enforcements

## Process documentation
See [examples](../examples)

## Governance

## Training

### War game

#### With CSIRT notification

#### Without CSIRT notification