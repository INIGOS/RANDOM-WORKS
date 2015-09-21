import pickle , re, collections ,os , sys , inspect , traceback
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
from Twokenize import twokenize
from Twokenize import emoticons
import itertools
path = cmd_folder+"/models/"

class Extraction(object):
    def __init__(self):
        self.acronyms=self.load_obj("acronymsDict")
        self.emoticons=self.load_obj("SmileyDict")
        self.answer={}
    def load_obj(self,name):
        with open( path + name + '.pkl' , 'rb') as f:
            return pickle.load(f)
    def EmoOperation(self,text):
        emo_list=[]
        acr_list=[]

        for word in twokenize.tokenize(text):
            if word !=" ":
                word=word.strip()

                try:
                    score=self.emoticons[word]
                    emo=emoticons.analyze_tweetHeavy(word)

                    emo_list.append(word)
                    emo_list.append(emo)
                    d=dict(itertools.izip_longest(*[iter(emo_list)] * 2, fillvalue=""))
                    
                except:

                    if "@" in word:
                        word="@user"
	return d 
    def AcroOperation(self,text):


        text=text.lower()
        store_acronyms = {}
        for word in twokenize.tokenize(text):
            if word !=" ":
                word=word.strip()

                try:
                    #print "before:", word
                    word_after=self.acronyms[word]
                    # acr_list.append(word)
                    #print "after:", word
                    store_acronyms[word] = word_after
                    # self.answer['ACRONYMS']=acr_list
                except:
                    if "@" in word:
                        word="@user"
            # print "EMOTICONS"
        self.answer['ACRONYMS'] = store_acronyms
        #return self.answer
	return store_acronyms
extract=Extraction()
text="hey hello :p , today is tuesday :) rofl and LOL the weather is :p too hot @ chennai :( :p lol , ok ciao "
output=extract.EmoOperation(text)
#replace EmoOperation by AcroOperation to get all the acronmys present in the given text
print output
