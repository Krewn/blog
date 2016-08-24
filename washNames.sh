#!/bin/bash

for f in *.html;do
	opName=${f// /_}
	opName=${opName/'?'/''}
	echo $opName
	mv "$f" "$opName"
done
