#!/bin/bash
# read the specified log file
# count '404' nums
# write lines with '404' to a specified file

DATETIME=$(date +%Y%m%d%H%M%S)

# specify argument(s) with '--path' and '--output'
for i in "$@"
do
  case $i in
    --path=*)
    PATH="${i#*=}"
    shift
    ;;
    --output=*)
    OUTPUT="${i#*=}"
    shift
    ;;
    *)
    ;;
  esac
  shift
done

if [[ -n ${PATH} ]];then
  echo -e "\033[32mInput Log Path: ${PATH}\033[0m"
else
  echo -e "\033[32mPlease input log path\033[0m"
  echo -e "\033[32m{USAGE: $0 --path=xxx.log [--output=/home/]}\033[0m"
fi

if [[ -n ${OUTPUT} ]];then
  echo -e "\033[32mOutput File Dir: ${OUTPUT}\033[0m"
else
  OUTPUT="/home/"
  echo -e "\033[32mOutput File Dir: ${OUTPUT}\033[0m"
fi

count=0
filepath="${OUTPUT}log_analysis-${DATETIME}.log"
echo -e "\033[32mOutput File Path: ${filepath}\033[0m"

echo "###### Log Analysis Result ######" >> ${filepath}

while read line
do
  if [[ "${line}" =~ "404" ]];then
    ((count++))
    echo ${line} >> ${filepath}
  fi
done < ${PATH}

/usr/bin/sed -i "1 a\\Total '404' nums: ${count}\n" ${filepath}

echo -e "\033[32mLog Analysis Complete!\033[0m"
