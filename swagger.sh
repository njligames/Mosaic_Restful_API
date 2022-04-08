#!/bin/bash

docker pull swaggerapi/swagger-editor
docker run -d -p 80:8080 swaggerapi/swagger-editor
open -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome http://localhost

