### password = Password123

### Commands via Permguard CLI:
#### antonioradesca@My-MacBook-Pro: permguard zones create --name demozone
197102289968: demozone
#### antonioradesca@My-MacBook-Pro:  permguard authz ledgers create --name sample --zoneid 197102289968
359f7ed82fac42f0a438f4f80174c52a: sample
#### antonioradesca@My-MacBook-Pro:  permguard authn identitysources create --name fastapi --zoneid 197102289968 
cf3980a8bb124b3a97ce30a06b44a739: fastapi
#### antonioradesca@My-MacBook-Pro:  ~:  permguard authn identities create --name johndoe --kind user --identitysourceid cf3980a8bb124b3a97ce30a06b44a739 --zoneid 197102289968 
5746fa72eaf84ec78997ead5bc179480: johndoe



### Workspace:
#### antonioradesca@My-MacBook-Pro:  ~/Desktop/fastapi3:  cd policies                                                                                                                ✔  10137  19:25:08 
#### antonioradesca@My-MacBook-Pro:  ~/Desktop/fastapi3/policies:  permguard init                                                                                                    ✔  10138  19:25:10 
Initialized empty permguard ledger in '.'.
#### antonioradesca@My-MacBook-Pro:  ~/Desktop/fastapi3/policies:  permguard remote add origin localhost                                                                             ✔  10139  19:25:23 
Remote origin has been added.
#### antonioradesca@My-MacBook-Pro:  ~/Desktop/fastapi3/policies:  permguard checkout origin/197102289968/sample                                                                     ✔  10140  19:25:29 
Ledger sample has been added.
The local workspace is already fully up to date with the remote ledger.
 antonioradesca@My-MacBook-Pro:  ~/Desktop/fastapi3/policies:  permguard validate                                                                                                ✔  10141  19:25:53 
Your workspace has been validated successfully.
#### antonioradesca@My-MacBook-Pro:  ~/Desktop/fastapi3/policies:  permguard plan                                                                                                    ✔  10142  19:26:02 
Initiating the planning process for ledger head/197102289968/359f7ed82fac42f0a438f4f80174c52a.
Planning process completed successfully.
The following changes have been identified and are ready to be applied:

        + 0bdab81786a11c7cae5abe3470e949047644413ce5fb642ac7378a154fcbee45 platform-editor
        + a53e81bdc0bbfe350f2a215911e041e5d17663f0aa358ece1c01b46deb1c9fed platform-viewer
        + 0268775a3d5471210d18e6ad071ef8c048ec8343ab95f7a3bd2804e6e83fbc74 platform-super-administrator
        + b7bd5b02c73dab1e40940ce1be5c6ef2691bb7b5ac4c40ec4d7b33a3392f8723 schema

unchanged 0, created 4, modified 0, deleted 0

Run the 'apply' command to apply the changes.
#### antonioradesca@My-MacBook-Pro:  ~/Desktop/fastapi3/policies:  permguard apply                                                                                                   ✔  10143  19:26:06 
Initiating the planning process for ledger head/197102289968/359f7ed82fac42f0a438f4f80174c52a.
Planning process completed successfully.
The following changes have been identified and are ready to be applied:

        + 0268775a3d5471210d18e6ad071ef8c048ec8343ab95f7a3bd2804e6e83fbc74 platform-super-administrator
        + 0bdab81786a11c7cae5abe3470e949047644413ce5fb642ac7378a154fcbee45 platform-editor
        + a53e81bdc0bbfe350f2a215911e041e5d17663f0aa358ece1c01b46deb1c9fed platform-viewer
        + b7bd5b02c73dab1e40940ce1be5c6ef2691bb7b5ac4c40ec4d7b33a3392f8723 schema

unchanged 0, created 4, modified 0, deleted 0

Initiating the apply process for ledger head/197102289968/359f7ed82fac42f0a438f4f80174c52a.
Apply process completed successfully.
Your workspace is synchronized with the remote ledger: head/197102289968/359f7ed82fac42f0a438f4f80174c52a.
