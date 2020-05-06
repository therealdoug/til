# MOQUERY

moquery is a command line utility on the Cisco APIC that can be used to pull information from the ACI MIT.

## Useful commands

### Compare Two Configurations for Differences  

Compare two EPGs:  
`diff <(moquery -c fvAEPg -f 'fv.AEPg.name=="KNX-MS-AD"' -a config) <(moquery -c fvAEPg -f 'fv.AEPg.name=="CHA-MS-AD"' -a config)`

```diff
ACI-APIC1# diff <(moquery -c fvAEPg -f 'fv.AEPg.name=="KNX-MS-AD"' -a config) <(moquery -c fvAEPg -f 'fv.AEPg.name=="CHA-MS-AD"' -a config)
4c4
< name                 : KNX-MS-AD
---
> name                 : CHA-MS-AD
```

Compare two BDs:  
`diff <(moquery -c fvBD -f 'fv.BD.name=="KNX-MS-AD"' -a config) <(moquery -c fvBD -f 'fv.BD.name=="CHA-MS-AD"' -a config)`
```diff
ACI-APIC1# diff <(moquery -c fvBD -f 'fv.BD.name=="KNX-MS-AD"' -a config) <(moquery -c fvBD -f 'fv.BD.name=="CHA-MS-AD"' -a config)        
4c4
< name                     : KNX-MS-AD
---
> name                     : CHA-MS-AD
8c8
< descr                    : Knoxville LDAP/Deadpool Config
---
> descr                    : Chattanooga LDAP/Deadpool Config
```

Compare full configuration:
``

```diff

```

#### 


# References

- [ACI Object MOQUERY Cheat Sheet](https://community.cisco.com/t5/data-center-documents/aci-object-moquery-cheat-sheet/ta-p/3367801)
- [Cisco ACI Policy Model Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/policy-model-guide/b-Cisco-ACI-Policy-Model-Guide.html)
- 