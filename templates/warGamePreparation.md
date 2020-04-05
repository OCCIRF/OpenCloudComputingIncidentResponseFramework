# Template: War Game Preparation 
This template helps to plan and conduct a war game. All needed details for one can be documented in the template for
further references.

## Template
> # War game: [name]
> ## General
>
> |                              |                          |
> |------------------------------|--------------------------|
> | Date:                        | [date]                   |
> | Type:                        | [ ] with Notification    |
> |                              | [ ] without Notification |
> | CSIRT management contact:    | [name]                   |
> |                              | [email]                  |
> | CSIRT management approval:   | [ ] Yes: [date]          |
> | Project name                 | [project name]           |
> | Project management contact:  | [name]                   |
> |                              | [email]                  |
> | Project management approval: | [ ] Yes: [date]          |
> | Attack team:                 | [group]                  |
> | Attack team members:         | [members]                |
>
> ## Technical details
>
> |                              |                          |
> |------------------------------|--------------------------|
> | Initial attack vector:       | [attack vector]          |
> | IPs / FQDNs                  | [IP / FQDN list]         |
>
> ### Scenario
> [scenario detail]
>
> ### Expected reaction
> [details to the expected reactions from the CSIRT]
>
> ## Attack tracker
>
> | Time                         | Details                  |
> |------------------------------|--------------------------|
> | [time]                       | Initial attack           |
> | [time]                       | [next step]              |

## Example
> # War game: Azure Portal credential theft
> ## General
>
> |                              |                          |
> |------------------------------|--------------------------|
> | Date:                        | 2020-02-02               |
> | Type:                        | [ ] with Notification    |
> |                              | [x] without Notification |
> | CSIRT management contact:    | John J.                  |
> |                              | John.J@corporation.com   |
> | CSIRT management approval:   | [x] Yes: 2020-01-15      |
> | Project name                 | really-important-web-app |
> | Project management contact:  | Hans W.                  |
> |                              | Hans.W@corporation.com   |
> | Project management approval: | [x] Yes: 2020-01-10      |
> | Attack team:                 | SEC/SRT                  |
> | Attack team members:         | Diana, Marco             |
>
> ## Technical details
>
> |                              |                          |
> |------------------------------|--------------------------|
> | Initial attack vector:       | Credential theft         |
> | IPs / FQDNs                  | portal.azure.com         |
>
> ### Scenario
> An attacker stole credentials via a phishing e-mail and uses it now to login to the Azure subscription. He then
> proceeds to use Azure resources and tries to steal data. 
>
> ### Expected reaction
> Monitoring alerts that the account is used from another IP. Alerting for resource miss usage. CSIRT blocks account.
>
> ## Attack tracker
>
> | Time                         | Details                  |
> |------------------------------|--------------------------|
> | 2020-02-02 9:00CEST          | Login from unknown IP    |
> | 2020-02-02 9:05CEST          | Starting some VMs        |
> | 2020-02-02 9:30CEST          | Downloading DB backups   |
> | 2020-02-02 9:45CEST          | Account got locked       |