# Template: War Game Evaluation 
This template helps to plan and conduct a war game. All needed details for one can be documented in the template for
further references.

## Template
> # War game: [name]
> Overall performance: [ ] 1 | [ ] 2 | [ ] 3 | [ ] 4 | [ ] 5
>
> ## Evaluation
>
> | Name                         | Details                  |
> |------------------------------|--------------------------|
> | Resolved:                    | [ ] Yes, [ ] No, 1)      |
> | Time to resolution:          | [time]                   |
> | CSIRT Feedback:              | [ ] Yes, 2)              |
> | Project Team Feedback:       | [ ] Yes, 3)              |
> | Judge feedback:              | [ ] Yes, 4)              |
> | Lessons learned:             | [ ] Yes, 5)              |
>
> ## Response tracker
>
> | Time                         | Details                  |
> |------------------------------|--------------------------|
> | [time]                       | First notification       |
> | [time]                       | [next step]              |
>
> ## Details
>
> ### 1. Resolution:
>
> ### 2. CSIRT Feedback:
>
> ### 3. Project Team Feedback:
>
> ### 4. Judge feedback:
>
> ### 5. Lessons learned:
>

## Example
> # War game: Azure Portal credential theft
> Overall performance: [ ] 1 | [ ] 2 | [ ] 3 | [x] 4 | [ ] 5
>
> ## Evaluation
>
> | Name                         | Details                  |
> |------------------------------|--------------------------|
> | Resolved:                    | [x] Yes, [ ] No, 1)      |
> | Time to resolution:          | 45 min                   |
> | CSIRT Feedback:              | [x] Yes, 2)              |
> | Project Team Feedback:       | [x] Yes, 3)              |
> | Judge feedback:              | [x] Yes, 4)              |
> | Lessons learned:             | [x] Yes, 5)              |
>
> ## Response tracker
>
> | Time                         | Details                  |
> |------------------------------|--------------------------|
> | 2020-02-02 09:10CEST         | Alert: Account activity  |
> | 2020-02-02 09:15CEST         | Alert investigation      |
> | 2020-02-02 09:35CEST         | Alert: Traffic activity  |
> | 2020-02-02 09:40CEST         | Contact account owner    |
> | 2020-02-02 09:45CEST         | Account got locked       |
> | 2020-02-02 10:00CEST         | Root cause analysis      |
> | 2020-02-02 10:10CEST         | War game end             |

>
> ## Details
>
> ### 1. Resolution:
> Account owner got contacted. The account got locked after clarifying that it was compromised.
>
> ### 2. CSIRT Feedback:
> The alert messages have a delay from approx. 10 minutes. This needs to be investigated.
>
> ### 3. Project Team Feedback:
> The account should be locked earlier before contacting the account owner as critical data was already downloaded.
>
> ### 4. Judge feedback:
> Alerts need to be checked. Expected reaction was fulfilled. Faster response to account miss usage is desirable.
>
> ### 5. Lessons learned:
> Alerts will be checked. Playbooks for this scenario will be updated.
>