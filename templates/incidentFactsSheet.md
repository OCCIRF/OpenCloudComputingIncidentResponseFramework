# Template: Incident Facts Sheet
This template helps to document all available information about an ongoing incident. 

## Template
```
# Incident: [incidentName]
## General

| Name                         | Details                  |
|------------------------------|--------------------------|
| Start:                       | [time]                   |
| Resolved:                    | [time]                   |
| Reporter contact:            | [reporter]               |

## Status

| Name                         | Status                   |
|------------------------------|--------------------------|
| Event classified:            | [ ] Yes: [status]        |
| Incident classified:         | [ ] Yes: [status]        |
| Triage conducted:            | [ ] Yes: [status]        |
| Affected parties contacted:  | [ ] Yes: [status]        |
| Incident contained:          | [ ] Yes: [status]        |
| Systems recovered:           | [ ] Yes: [status]        |
| Root cause found :           | [ ] Yes: [status]        |
| Lessons learned conducted:   | [ ] Yes: [status]        |
| Documentation finished:      | [ ] Yes: [status]        |

 ## Technical Details

| Name                         | Details                  |
|------------------------------|--------------------------|
| Impact:                      | [impactRating]           |
| Urgency:                     | [urgencyRating]          |

### Affected Systems

### Affected Parties

### Root Cause

### Lessons Learned

### Documentation Link


## Response Tracker

| Time                         | Details                  |
|------------------------------|--------------------------|
| [time]                       | [step]                   |
| [time]                       | [step]                   |
```

## Example
> # Incident: Possible Azure credential theft
> ## General
>
> | Name                         | Details                  |
> |------------------------------|--------------------------|
> | Start:                       | 2020-02-02 09:10CEST     |
> | Resolved:                    | 2020-02-02 10:10CEST     |
> | Reporter contact:            | SIEM Alert               |
>
> ## Status
>
> | Name                         | Status                   |
> |------------------------------|--------------------------|
> | Event classified:            | [x] Yes: Confirmed       |
> | Incident classified:         | [x] Yes: 9               |
> | Triage conducted:            | [x] Yes: Account found   |
> | Affected parties contacted:  | [x] Yes: Team            |
> | Incident contained:          | [x] Yes: Account locked  |
> | Systems recovered:           | [ ] Yes: [status]        |
> | Root cause found :           | [ ] Yes: [status]        |
> | Lessons learned conducted:   | [ ] Yes: [status]        |
> | Documentation finished:      | [ ] Yes: [status]        |
>
> ## Technical Details
>
> | Name                         | Details                  |
> |------------------------------|--------------------------|
> | Impact:                      | 3 - Major                |
> | Urgency:                     | 3 - Major                |
>
> ### Affected Systems
> very-important-web-app Azure account
>
> ### Affected Parties
> Project team: very-important-web-app
>
> ### Root Cause
> \- 
>
> ### Lessons Learned
> \- 
>
> ### Documentation Link
> \- 
>
> ## Response Tracker
>
> | Time                         | Details                  |
> |------------------------------|--------------------------|
> | 2020-02-02 09:10CEST         | Alert: Account activity  |
> | 2020-02-02 09:15CEST         | Alert investigation      |
> | 2020-02-02 09:35CEST         | Alert: Traffic activity  |
> | 2020-02-02 09:40CEST         | Contact account owner    |
> | 2020-02-02 09:45CEST         | Account got locked       |
> | 2020-02-02 10:00CEST         | Root cause analysis      |
> | 2020-02-02 10:10CEST         | End because of war game  |
>