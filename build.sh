#!/bin/bash
STANFORD_SEGMENTER_JAR='/home/wlzhuang/stanford-segmenter-2015-04-20/stanford-segmenter-3.5.2.jar'

pip3 install Jpype1

javac -cp "$STANFORD_SEGMENTER_JAR" \
  -d chineseseg chineseseg/DemoSeg.java


