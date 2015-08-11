import chineseseg



string = "蘇迪勒颱風造成土石崩塌，供應台北市用水的南勢溪挾帶大量泥沙，原水濁度一度飆高。"



ckip = chineseseg.Ckip("myaccount", "mypassword")

stanford = chineseseg.stanford("/home/wlzhuang/stanford-segmenter-2015-04-20/stanford-segmenter-3.5.2.jar", debug=True)


print( "stanford:", stanford.segment(string) )
print( "ckip:", ckip.segment(string) )


