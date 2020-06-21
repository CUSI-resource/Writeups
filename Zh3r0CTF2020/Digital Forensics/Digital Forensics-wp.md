# PreDestination
Description:MR.Zh3r0 is a mathematician who loves what he does, he loves music and he is fairly good; like an average joe, with personal desktops but a really gullible person who could be phished or scammed easily! He had some bad colleagues in his office that led him to have some bad intentions towards them. One of his "HECKER" friend suggested to download some virus to destroy the data the other people has. As you would expect, this backfired. He has called the World's best forensics experts to come to his rescue! We were fortunately able to get his PC's image and some of the files in it. And We have a suspicion if he only downloaded one malware or more than one? And we need answers to some questions that follow, this would be your first assignment!  
We found that his PC had some sort of problem with Time Zones even though he tries to reset it, it seems the malware is somehow able to edit the TimeZone to the malware author's name. How could a malware edit the TimeZone information if it had Administrator Privilege to the system!?  
Note:- File for the challenges in this series is the same  
Author : Amun-Ra  
Flag format - zh3r0{authorname}  
File Link:https://drive.google.com/drive/folders/1ZfKCOAm3OcmG8oLZt37DhN-FyMS14QaK 

The challenge description mentions Timezones, and about how the Timezone is changed to the malware author name, which is the flag.  
So we want to look for the TimeZone registry entry, typically found in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation.  
Under the StandardName key, we see the value Cicada3310, which is the flag.  
zh3r0{Cicida3310}