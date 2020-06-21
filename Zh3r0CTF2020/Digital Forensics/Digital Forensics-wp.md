# PreDestination
The challenge description mentions Timezones, and about how the Timezone is changed to the malware author name, which is the flag.  

So we want to look for the TimeZone registry entry, typically found in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation.  

Under the StandardName key, we see the value Cicada3310, which is the flag.  
zh3r0{Cicida3310}