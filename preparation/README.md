# Incident preparation
The preparation is an integral part of the incident response process. Here you need to plan and prepare your strategy
and your tools. 
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

Those fact sheets can be stored in an asset management tool or a simple database (See [examples/assetManagement](../examples/assetManagement.md)). 
Also, an offline version is possible as in an incident case it is not guaranteed that the online asset management tools
are accessible (See [templates/assetFactsSheet](../templates/assetFactsSheet.md)).  
The more precisely the facts sheets are the easier it is to get all needed assets in an incident case. To assure that
all facts sheets are up to date a periodic review should be done.
   
## Roles and responsibilities
Defined responsibilities are important in an incident process as all involved persons need to know what they need to do.
The employees within the set responsibilities should be skilled to handle those in a pressure situation like an incident
event. The roles and responsibilities should also be documented. An example document can be found [here](../templates/rolesAndResponsibilities.md).

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
writes press releases or notifications to customers if they are affected. Also, an important communication partner are the
law enforcements as legal responsibilities are needed to be followed (Like GDPR or KRITIS in Germany). He is responsible
for internal communications, too. E.g. communicating the comments on the incident and the affected systems to the internal
employees.

#### Trainers
It is very important to train the different departments regarding incident response and general security. If there is no
ongoing incident the team members of the incident response team should train the colleagues to improve the security
knowledge. The trainers are not relevant for an incident, but they are helping a lot to prevent those.

### Other internal departments
#### Legal Manager
The legal manager is responsible for legal questions for the incident. He as to provide contact details to authorities to
the communication manager or work with him together on statements for them. He can also consult the management, or the
incident response team in legal questions.Moreover, he needs also help the team in GDPR topics if there is no dedicated
department for data protection in the organisation.

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

#### Point of contact

## Access concept
The access concept for incident response is an interesting topic. Here it is important to guarantee quick reaction times
but also honor the least privileges principle. 

## Communication

### Communication to the cloud provider

### Internal communication

### Communication to customers

### Communication to law enforcements

## Governance

## Training

### War game

#### With CIRT notification

#### Without CIRT notification