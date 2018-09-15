import socket
#from urllib.parse import urlsplit, parse_qs
import test
import json
import os
#from furl import furl
from w3lib.url import url_query_parameter

host = ''
port = 3126
CLRF = b'\r\n'


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.listen(5)
# prevText = {}
# prevReply = {}
# people = []
    
"""
The request should be of the format- http://127.0.0.1:3126/?query=somestring&id=somenumber

"""

def startListening():
    # global prevReply
    # global prevText
    
    print("Listening")
    try:
        client, addr = serverSocket.accept()
        
    except KeyboardInterrupt:
        client.close()
        return
    except Exception as e:
        print("Could not establish connection with the client", e)
    finally:
        pass

    try:
        client.send(b'HTTP/1.1 200 OK' + CLRF)
        client.send(b'Content-Type: text/html' + CLRF*2)
        request = client.recv(1024)
        #getRequest = request.splitlines()[0].decode("utf-8")[4:-9]
        #print(getRequest)
        #query = urlsplit(getRequest).query
       # print(query)
        #parameters = parse_qs(query)
        #print(parameters)
    except KeyboardInterrupt as e:
        print(e)
        return
    except Exception as e:
        print("Error whilefsa parsing the GET Request", e)

        return
    finally:
        pass
    
    try:
       # question = parameters["query"][0]
        #question=str(url_query_parameter(getRequest, 'query'))
        # chatID = parameters["id"][0]
       # print(question)
       print("executing")
        
    except KeyboardInterrupt as e:
        print(e)
        return
    except Exception as e:
        print("Either the query, or id parameters haven't been passed. Make sure the request is x.x.x.x", e)
        return
    finally:
        pass
    
    try:
        reply={}
        os.system("py ask.py")
        #os.system("py finalask.py"+" "+"'"+str(question)+"'")
        #reply = test.response(question)
        print(reply,"reply")
       
        # if (question == "/wrong"):
        # #     error = "id-" + chatID + "-txt-" + prevText[chatID] + "-rep-" + prevReply[chatID] + '\n'
        # #     with open("SockErrors.txt", 'a') as file:
        # #         file.write(error)
        #     return
        # # prevText[chatID] = question
        # # prevReply[chatID] = reply
        
    except Exception as e:
        print("Error while parsing GET Request", e)
        print("The value passed to the Bot was not defined fsa")
    finally:
        pass
    
    try:
        print(reply)
        
        replyDict = {'text': {'sync': True, 'type': 'change_slide', 'data': 1}}
        # questionDict=
        # questionDict=dict([("Text",question)])
        # # if chatID not in people:
        # #     reply = "Hello!  You seem to be a new face, allow me to introduce myself. I am BOSSBOT.\
        # #            What can i help you with?"
        # #     people.append(chatID)
        # # if reply == "":
        # #     reply = "I'm sorry, I didn't understand you. Could you rephrase it please?"
        # # replyDict["reply"] = reply
        # replyDict = json.dumps(reply)
        # questionDict=json.dumps(questionDict)
        # print(replyDict,"replyDictionary",questionDict)
    except Exception as e:
        print("Error while parsing GET request", e)
    try:
        string ="vinod"
       # print(replyDict.encode())
        #print(questionDict.encode())
        # client.send(questionDict.encode())
        client.send(string.encode())
    except KeyboardInterrupt as e:
        print(e)
        return
    except Exception as e:
        print("Could not send reply to client", e)
    finally:
        pass
    
    client.close()


while True:
    startListening()

serverSocket.close()
