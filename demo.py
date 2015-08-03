import chineseseg

"""
stanford = chineseseg.stanford("/home/wlzhuang/stanford-segmenter-2015-04-20/stanford-segmenter-3.5.2.jar")
print( stanford.segment("简单调用情况如下") )

"""
import socket
from lxml.etree import tostring, fromstring
from lxml.builder import E
class Ckip():

    CKIP_SERVER_IP, CKIP_SERVER_PORT = "140.109.19.104", 1501

    def __init__( self, username, password, server_ip = CKIP_SERVER_IP, server_port = CKIP_SERVER_PORT ):
        self.username = username
        self.password = password

        self._server_ip = server_ip
        self._server_port = server_port

    def segment( self, sent ):
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        sock.connect( (self._server_ip, self._server_port) )

        encoding = "big5"
        tree = E.wordsegmentation(
            E.option(showcategory='1'),
            E.authentication(username=self.username, password=self.password),
            E.text(sent),
        version='0.1')
        xmlstring = tostring(tree, encoding=encoding, xml_declaration=True)


        sock.send( xmlstring )
        data = sock.recv( 10240 )
        sock.close()
        return self.parse_result( data.decode(encoding) )

    def parse_result( self, string ):
        return string



seg = Ckip("wlzhuang", "xxxxaaaackip")
print( seg.segment("本線上斷詞服務的資料交換方式採用一XML格式，用戶端可自行撰寫程式經由 TCP Socket 連線傳送驗證資訊及文本至本伺服器，伺服器經過處理後經由原連線傳回結果。請詳閱以下說明：") )
