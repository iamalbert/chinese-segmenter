import chineseseg

segmenter = chineseseg.stanford("/home/wlzhuang/stanford-segmenter-2015-04-20/stanford-segmenter-3.5.2.jar")

print( segmenter.segment("简单调用情况如下") )
