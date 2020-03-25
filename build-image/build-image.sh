#!/bin/sh
set -e
tag="v1"
rm -rf hadoop-ozone
git clone https://github.com/apache/hadoop-ozone.git
cd hadoop-ozone
mvn clean package -DskipTests=true
cd ..
rm -rf ozone
mv hadoop-ozone/hadoop-ozone/dist/target/ozone-0.5.0-SNAPSHOT ozone
docker build -t="ozone:${tag}" .
docker ozone:${tag}
