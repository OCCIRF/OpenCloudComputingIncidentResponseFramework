# Template: Emergency Access
This template helps to document a request for emergency access to a cloud account. 

## Template
```
# Emergency Access

## Information

| Name                         | Details                  |
|------------------------------|--------------------------|
| Requester:                   | [requester]              |
| Incident Id:                 | [Incident Id]            |
| Processor:                   | [IdM processor]          |
| Granted:                     | [ ] Yes, [ ] No          |

### Justification for granting/rejecting the access
[Justification]

## User List:
[List of users with emergency access]

## Timetable

| Name                         | Details                  |
|------------------------------|--------------------------|
| Request:                     | [time]                   |
| Granted:                     | [time]                   |
| Revoked:                     | [time]                   |
```

## Example
> # Emergency Access
> 
> ## Information
> 
> | Name                         | Details                  |
> |------------------------------|--------------------------|
> | Requester:                   | Joe Mueller              |
> | Incident Id:                 | INC-20200202-0910        |
> | Processor:                   | Kira Schmidt             |
> | Granted:                     | [x] Yes, [ ] No          |
> 
> ### Justification for granting/rejecting the access
> Investigation and containment
> 
> ## User List:
> * Joe Mueller (joe@example.com)
> * Mara Gates (mara@example.com)
> 
> ## Timetable
> 
> | Name                         | Details                  |
> |------------------------------|--------------------------|
> | Request:                     | 2020-02-02 09:45CEST     |
> | Granted:                     | 2020-02-02 09:50CEST     |
> | Revoked:                     | 2020-02-02 11:00CEST     |