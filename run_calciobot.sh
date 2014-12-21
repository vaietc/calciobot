#!/bin/sh

# Edit to 0 if you do not want it to sync with git, otherwise 1 to sync
UPDATE_FROM_GIT=1	

# Update with the directory where the calciobot is location
SCRIPTDIR="${HOME}/calciobot"

# Do not edit below this line, unless you know what you are doing
SCRIPTLOG="${SCRIPTDIR}/ssbbot.log"
SCRIPTNAME="./ssbbot.py"

cd ${SCRIPTDIR}
echo -e "\n\n########################\n# Started: `date`" >> ${SCRIPTLOG}
if [ "${UPDATE_FROM_GIT}" == "1" ] ; then 
  git fetch >> ${SCRIPTLOG}
  git pull >> ${SCRIPTLOG}
else 
  echo -e "Skipping syncing with git"
fi

python ${SCRIPTNAME} >> ${SCRIPTLOG}
echo -e "\n# Ended: `date`\n########################" >> ${SCRIPTLOG}
