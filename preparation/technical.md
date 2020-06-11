# Technical Incident Preparation
After the organisational preparation is done the tools and technical settings can be done to prepare the incident
response process. This chapter is focusing on this.

{ToC}

## Logging
An important part, if not the most important part of the technical preparation is to prepare the logging process. In
cloud environments logs are most of the time the source of truth for actions happening in the cloud. Also, if platform
services are used it is most likely the case that the administrator, nor the security team has access to the file system
to analyse security events with forensic tools.  
The log entries are one of the most important source of information about the health of a system and a great indicator
of a possible compromise or other incident. Log files are there to trace certain events through an application and whole
environments. Therefor log files need to be central aggregated and configured to have e.g. the same time source and time
zone.  
Further more log entries needs to be protected from manipulation or deletion from unauthorized parties.

### Log aggregation
With the separation of different development projects into different subscriptions or accounts a centralized logging and
investigation platform has to be established. This should be done in a separate subscription or account where the CSIRT
can then correlate all needed events. The central correlation is important to see attacks in different environments.
E.g. An IP address is generating suspicious events in one environment, with central logs it can be checked if this IP is
also targeting different environments.

![Central logging](logging.png)

For this central logging approach the CSIRT or another SOC Team has to provide a central solution where all project
teams can send their log to. Examples can be found [here](../examples/centralLogging.md).

### Log sharing

### Log analysis
When the log files are centrally stored they can be analysed. Without analysing the log files no events can be found and
reacted to. Log analysis is the step where the raw log lines gets correlated with each other and analysed for malicious
behavior or known patterns. 

#### SIEM
A Security Information and Event Management (SIEM) System is a tool which helps to analyse and correlate log events.
Those tools are great to manage all sorts of events and log sources for the environments. Also, alerts can be generated
easily in those systems to notify the on-call teams in an emergency event.  
Most cloud providers have a SIEM solution in their portfolio. Furthermore, open source products or 3rd party products
are also available. Examples can be found [here](../examples/siem.md).

#### Playbooks
After the log files are stored and processed centrally, playbooks can be defined. Playbooks are a set of rules which
will trigger actions when specific log events pop up. These actions can be only notifications to the security analyst or
specific actions like locking an account. These playbooks need to be tailored for the needs of the environment and the 
CSIRT. Examples can be found [here](../examples/playbooks.md).

## Monitoring
Not only log events are helping find events, also monitoring of the cloud environment can give indicators of compromise.
Monitoring helps visualise trends for the monitored KPIs. Those KPIs might be:
 * Costs of the booked services
   * Here a malicious actor might started services to mine e.g. crypto currencies 
 * Utilization of resources (CPU, RAM, Storage)
   * High utilization of CPU usage might be caused by a DOS attack or some malicious software
 * Network usage (in- and outgoing traffic, sessions, delays)
   * Higher than normal traffic might be caused by data exfiltration (outgoing traffic) or a DOS attack (incoming
   traffic)
 * Service availability (Host checks, network availability)
   * Non responsive hosts might be caused by a DOS attack, a manipulation of the system or a host failure

Monitoring examples can be found [here](../examples/monitoring.md).

## Visibility
Not only is it important, that log files are sent to a central logging tool but also that logs are generated. Before
logs are generated information needs to be visible in the environment to be able to be picked up by the logging tools.  
Here the developers and the operations team are in duty to provide the necessary information to the logging and
monitoring systems. To force the developers and project teams to implement those measures a corporate policy might be
helpful. 
 
## Data extraction concept

## Access

## Response Tool Chain
