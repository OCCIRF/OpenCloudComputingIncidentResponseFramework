# Handling an Incident
Handling an incident in the cloud is the most different part for the incident response process compared to the
on-premises world. The reason for this is, that the responsibility for the systems is shared between the cloud service
provider and the cloud service customer. Infrastructure-as-a-service it is still comparable to the on-premises process.
Incident response for Platform-as-a-service is more restricted and different. The software-as-a-service model has the
lest possibilities for the customers to conduct incident response. Most of the time it is impossible to investigate the
incident as a customer.  
For the handling of the incident response a [template](../templates/incidentFactsSheet.md) is available to document the
incident.

## Event Input
The input events for the incident handling can be from multiple sources:
* An Event from the logging tools
* An internal notification
* An external notification

Those events are pre-classified by the log analysis tool and should only alert deviations from normal usage. Also, event
classified in the play books should be part of the alerts.

## Classification
In the classification phase the alerted event is investigated. Here the CSIRT should classify the event with the
previous defined patterns it is an incident. If the event is not an incident a root-cause analysis should be done why
the event was alerted. Reasons for that can be many:
* It was a false-positive from the log analysis
* The environment got changed
* The cloud provider changed something on their side
* The alerting system is broken
* The boundaries for an alert are too wide

When the root-cause for the false-positive alert is done the alerting system should be updated and the change and the
event needs to be documented.  
If the event is an incident the incident needs to be classified as described in the corporate policies. The
classification is then the baseline for the further actions and who will be alerted.  

## Triage
The event classification and the triage go hand in hand. While in triage of the event the CSIRT needs to carefully
but fast analyse the impact of the incident. This needs to be done to find out what happened and which systems are
affected. The list of affected systems is the baseline of the actions of the containment. For the triage the logs are
again the source of truth in cloud environments. ..... ***Triage checklist?***

## Containment
The containment is the most different part of the incident response compared to the on-premises incident response. 
On-premises it is possible to plug out the servers in the worst case scenario. In the cloud environment this is not
possible. The containment is also very different between the three service models provided in the cloud (IaaS, PaaS,
SaaS). It is very important to document the steps done in the containment phase. This documentation is later needed for
the recovery and the reconstruction of the incident.

### IaaS
Infrastructure-as-a-Service is the service model which is the nearest to the on-premises world. When a IaaS component is
compromised it can be isolated in a virtual network or disconnected through firewall rules from the internet. Also, most
of the time the traffic in virtual networks can be sniffed to gather more information about the incident. 

### PaaS
When using Platform-as-a-Service the used service might not have a virtual network integration or are able to set 
firewall rules. In those cases the containment needs to be done on an application level. This might be revoking access
tokens to the services or ad-hoc fixing the issue which causes the incident.  

### SaaS
As a Software-as-a-Service customer the incident response capabilities are very limited as the whole software is
controlled by the SaaS provider. Normally the customer can only rely on the skills of the SaaS provider and hope that he
can resolve the incident. If the SaaS solution is connected to the central identity management via a federation solution
it is possible to lock the access to the solution for all employees to prevent further damage. Also, all connections to
the service should be revoked. 

## Eradication / Recovery
After the incident is contained the environment needs to be cleaned up. This means that all changes made by the
intrusion needs to be found and eliminated. The best option is to nuke the environment and rebuild a new version with
backups from before the incident. If this is not possible each service needs to be inspected if the intrusion changed
something there. To help analyse the incident it is also possible to rebuild the environment in a different subscription
or account. The compromised environment can then be used for a forensic analysis.

## Reconstruction / Root-Cause Analysis
While reconstructing the incident the CSIRT needs to find out exactly what happened. This is the forensics part of the
incident response. Here the root-cause needs to be found and the attack tracked. Before doing the root-cause analysis
the team needs to decide if it needs to be evidential for law-enforcements or only an internal commitment.  
To conduct the root cause analysis a few things have to be taken care of. First the cloud services are often not easy
accessible (E.g. analysing the stored data or live analysis of the ram). Secondly they are stripped down most of the
time, so they only provide necessary tools for their job. Also, a lot of the cloud services (Like Azure Web App) are
based on containers which will be redeployed once they crash or after a given amount of time. This then also deletes 
all evidence of a possible breach services based on those platforms. 