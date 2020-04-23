#!/bin/bash

if [ "$#" -lt 1 ]
then
echo "Usage: $0 <zipfiles...>"
exit 1
fi

for f in $@
do

 stored=`cat $f.md5`
 downloaded=`md5sum $f`

 stored=${stored%%\ *} 
 downloaded=${downloaded%%\ *} 

 if [ ! "$stored" = "$downloaded" ]
 then
   echo "FAILED: $f"
 fi
done
