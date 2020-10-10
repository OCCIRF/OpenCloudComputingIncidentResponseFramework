# Playbook examples
These are examples how playbooks might be set up for the cloud. Those playbooks are at a higher level and need to be
adapted to the used cloud provider.  
The mitigation steps are possible solutions for the event. They can and should be adapted according to the situation.

## Platform and accounts

| Source        | Indicator                           | Possible Incident | Mitigation Steps                |
|---------------|-------------------------------------|-------------------|---------------------------------|
| Billing alert | The account spending rises abnormal | Account takeover  | 1. Find the source of the spending<br>2. Get the initiator<br>3. Clarify it is intentionally<br>4. Block the account and clean the resources |
| Resource Monitoring | Spikes in the resource usage  | Breach, Crypto mining, DoS | 1. Find the affected resource<br>2. Check if the usage is normal<br>3. Isolate the resource (E.g. block incoming traffic)<br>3. Find the origin |
| Audit logging | Manual resource creation in an automated environment | Account takeover, hostile employee | 1. Find the source account <br>2. Block the account |  
| Access log | Login tries from another continent | Account takeover | 1. Lock the account<br>2. Clarify if this was a false-positive |
| Access log | Many failed login attempts | Account brute-force | 1. Blacklist the source IP<br>2. Throttle account login attempts | 

## Application

| Source        | Indicator                           | Possible Incident | Mitigation Steps                |
|---------------|-------------------------------------|-------------------|---------------------------------|
| Database log  | High amount of failed queries       | SQL injection attempt | 1. Control application and check the queries<br> 2. Block the source IP<br>3. Fix the issue which causes the failed queries |
| Database log  | Unusual high amount of queries      | SQL injection attempt | 1. Control application and check the queries<br> 2. Block the source IP |
| Resource Monitoring | High application or database load | DoS, injection attempt | 1. Find the cause of the load<br>2. Isolate the resource<br> |
| Flow log      | Request to unknown endpoint | Breach, malware, Reverse shell | 1. Capture the request<br>2. Terminate the connection<br>3. find the source |
| Application log | High amount of application errors | DoS, application breach attempt | 1. Analyze the errors<br>2. Block the user<br> 3. Fix the entry point |
 



