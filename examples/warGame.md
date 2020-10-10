# War Game Examples
Here you can find examples of war games which can be done to test parts of the incident response process. The following
examples are small snippets which can be used to test the incident response process. They can also be combined to a big
war game to test the teams and the process in a more detailed way.

## Suspicious log-ons
Suspicious log-ons are a great indicator of compromise. To test if this is alerted correctly an admin user can log-on to
the cloud environment from different countries using a VPN. This should trigger an alert, that the account might be
stolen.

## High outgoing data transfer
The cloud environment can be configured, that it is possible to transfer dummy data to another system outside of the own
environment. This action is an indication of compromise.  
Here an administrator opens an API or an interface where he then can copy data to another storage in the cloud. Ideally
a logging tool should alert here for this malicious traffic.

## High cost of cloud resources
A user can set up cost intensive cloud resources. If those resources are deviating a lot from the normal resource usage
an alert should be generated and the incident response process should start.

## Penetration test as a war game
Applications should regularly be penetration tested by a professional penetration tester. This penetration test can be
extended to a war game. In this scenario the penetration tester does his normal work and the incident response team
should see this as a normal attack and needs to start mitigating the impact.

## Two incidents at once
A good indication how efficient the process is, is to have two incidents at once. This help to find ineffective parts of
the process and the incident response team.

## Critical changes in the cloud infrastructure
Some changes in the cloud infrastructure might be critical like exposing management interfaces to the internet (e.g. SSH
or a kubernetes management interface). If critical changes are made an alert should be triggered, and the changes needs
to be investigated.