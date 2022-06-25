#!/bin/bash

URL=http://localhost:5000/api/timeline_post

for COUNT in {1..5}
do
curl -X POST $URL -d "name=testname${COUNT}&email=test${COUNT}@email.com&content=testcontent${COUNT}"
sleep $(( RANDOM%10+10 ))
done

curl $URL 