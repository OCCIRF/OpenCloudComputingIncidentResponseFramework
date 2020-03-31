# Template: Asset Facts Sheet
The asset facts sheet can help identify compromised or attacked systems. Further more it contains contacts fot the asset
and documentation for this asset.

## Template
```
# Asset Facts Sheet: [asset name]
Next review: [State next review]  

## General Facts

| Fact name          | Fact              |
| ------------------ | ----------------- |
| Description:       |                   |
| Owner:             |                   |
| Emergency contact: |                   |
| Criticality level: |                   |
| Provider:          |                   |
| Provider contact:  |                   |

## Technical Facts

| Fact name          | Fact              |
| ------------------ | ----------------- |
| IP(s):             |                   |
| Url(s):            |                   |
| Parent asset:      |                   |
| Child assets:      |                   |

## Documentation

| Fact name          | Fact              |
| ------------------ | ----------------- |
| Architecture:      |                   |
| Operations Manual: |                   |
| Threat model:      |                   |
| Penetration test:  |                   |

```

## Example
> # Asset Facts Sheet: really-important-web-app
> Next review: 01.2021  
> 
> ## General Facts
> 
> | Fact name          | Fact                                                                       |
> | ------------------ | -------------------------------------------------------------------------- |
> | Description:       | Our only web application where we make money with                          |
> | Owner:             | Mr. President                                                              |
> | Emergency contact: | Some IT-Dude (-0123)                                                       |
> | Criticality level: | critical (4)                                                               |
> | Provider:          | Azure                                                                      |
> | Provider contact:  | EmergencyContact@azure.com                                                 |
> 
> ## Technical Facts
> 
> | Fact name          | Fact                                                                       |
> | ------------------ | -------------------------------------------------------------------------- |
> | IP(s):             | 127.0.0.0/25, 192.168.0.0/28                                               |
> | Url(s):            | [www.example.com]()                                                        |
> | Parent asset:      | Productive-Subscription (00000000-0000-0000-0000-000000000000)             |
> | Child assets:      | [really-important-web-app-database](), [really-important-web-app-app]()    |
> 
> ## Documentation
> 
> | Fact name          | Fact                                                                       |
> | ------------------ | -------------------------------------------------------------------------- |
> | Architecture:      | [internal.example.com/confluence/really-important-web-app/architecture/]() |
> | Operations Manual: | [internal.example.com/confluence/really-important-web-app/ops-manual/]()   |
> | Threat model:      | [internal.example.com/dms/threat-models/really-important-web-app/]()       |
> | Penetration test:  | [internal.example.com/dms/pen-test/really-important-web-app/]()            |
