#!/bin/bash

MARKDOWN_FILE="/Users/nmichel/Library/CloudStorage/OneDrive-SharedLibraries-Cisco/Amazon Account Team - Amazon Web Services AWS/Projects and Technical/Lab/RTP Dcloud/Documentation/AWS-DX-RTP-LAB.md"
HTML_FILE="/Users/nmichel/Library/CloudStorage/OneDrive-SharedLibraries-Cisco/Amazon Account Team - Amazon Web Services AWS/Projects and Technical/Lab/RTP Dcloud/Documentation/AWS-DX-RTP-LAB.html"

echo $MARKDOWN_FILE | entr pandoc -s "$MARKDOWN_FILE" -o "$HTML_FILE"



