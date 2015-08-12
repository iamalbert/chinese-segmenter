import chineseseg



string = "協議草案已呈交希臘國會審議，最晚將於13日過關或與相關的改革包裹立法合併通過，而歐元區19國財長會議料將在14日予以認可，再經以德國為首的歐元區泰半成員國的國會批准。倘若一切順利，首筆紓困貸款釋出後，希臘將得以償付20日到期的歐洲中央銀行欠債32至34億歐元，避免債務違約。"



ckip = chineseseg.Ckip("username", "password")

stanford = chineseseg.stanford("/home/wlzhuang/stanford-segmenter-2015-04-20/stanford-segmenter-3.5.2.jar", debug=True)

print( "stanford:", stanford.segment(string) )
print( "stanford (sim):", stanford.segment(string, tosim=True))

print( "ckip:", ckip.segment(string) )
print( "ckip:", ckip.segment(string, segsent=True) )


