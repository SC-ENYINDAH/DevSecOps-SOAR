#!/bin/bash

STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000)

if [ "$STATUS" = "200" ] || [ "$STATUS" = "302" ]; then
    echo "Application Available"
else
    echo "Application Down"
    exit 1
fi
