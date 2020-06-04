# Technical Incident Preparation
After the organisational preparation is done the tools and technical settings can be done to prepare the incident
response process. This chapter is focusing on this.

{ToC}

## Log preparation
An important part of the technical preparation is to prepare the logging process. The log entries are one of the most
important source of information about the health of a system and a great indicator of a possible compromise or other
incident. Log files are there to trace certain events through an application and whole environments. Therefor log files
need to be central aggregated and configured to have e.g. the same time source and time zone.  
Further more log entries needs to be protected from manipulation or deletion from unauthorized parties.

### Log aggregation
With the separation of different development projects into different subscriptions or accounts a centralized logging and
investigation platform has to be established. This should be done in a separate subscription or account where the CSIRT
can then correlate all needed events. The central correlation is important to see attacks in different environments.
E.g. An IP address is generating suspicious events in one environment, with central logs it can be checked if this IP is
also targeting different environments.

![Central logging](logging.png)

### Log sharing

### Log analysis

#### Playbooks

#### SIEM

## Monitoring

## Visibility

## Response tool chain

## Data extraction concept

## Access

## Tools
