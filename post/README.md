# Incident Post-Processing
When the incident is properly handled and all system are back to nominal operation the post-processing can start. In
this phase of the incident response the whole event gets finalised.


## Lessons Learned
Lessons learned is an important tool for learning and improving. After each incident a "lessons learned" meeting should
be conducted. In this meeting the whole event should be reviewed to find possible errors or improvements in the process.
This meeting is not for shaming CSIRT team members or members from the project or operation. In the meeting the event
should be laid out to discuss what happened exactly at what times. This can then be used as a baseline to answer e.g.
following questions (partly taken from the NIST SP-800-61):
- Did the process work and was it followed?
- How was the overall performance?
- How was the communication between the CSIRT and external parties?
- Was information missing to any given time?
- What could have been better?

The answers to those questions can then be included in the training documentation to train new employees. Also, the
outcome of this meeting can be used to build slides for the management as an explanation what happens and why it won't
happen again.

## Documentation
After the incident is finalised it needs to be documented. The documentation should contain all detail which are
important for tracing the event. It should also contain all involved parties in the incident.  
A baseline for a good documentation is that someone who was not involved in the incident understands with only the
documentation what happened, what was done and who was involved.
A template can be found [here](../templates/incidentFactsSheet.md).

## Enhancement of the Organisation
All incidents have a root-cause which might be preventable. The information how the incident started is important for
other cloud users to prevent that from happening in their environment. The notification for that can be sen to the
cloud environment administrators via e-mail
([Example](../examples/communication.md#notification-to-project-teams-and-system-administrators)) or some other
messaging tools (like Slack or MS Teams notification).  
Also, most cloud providers also offer policy tools where an organisation administrator can create policies which are
enforced in the environments as alerts or direct changes (E.g. Azure policy or AWS config rules).