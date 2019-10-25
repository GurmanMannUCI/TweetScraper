
def ParserInfoWriter(PersonInfo):
    file = open("ParserInfo.txt",'w')
    file.write(str(PersonInfo))
    file.close()

def ParserInfoReader():
    maindict = {}
    try:
        file = open("ParserInfo.txt",'r').read()
        maindict = eval(file)
    except:
        pass
    return maindict

def TweetFileReader():
    maindict = dict()
    try:
        file = open("tweetfile.txt",'r').read()
        maindict = eval(file)
    except:
        pass
    return maindict

def TweetFileWriter(maindict):
    file = open("tweetfile.txt",'w')
    file.write(str(maindict))
    file.close()

