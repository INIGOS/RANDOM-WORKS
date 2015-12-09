from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime
import logging
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
logging.basicConfig(filename='kafka.log',level=logging.DEBUG)
logging.debug("This message should go to the log file")
logging.info("so should This")
logging.warning("and this too ")

#consumer key, consumer secret, access token, access secret.
ckey="CEA1R5SZILxvV4bmz8cBs9eJt"
csecret="WgCaMBV4PlO83VSQs1tL4FuL5Splaywj3qdtuUr3hT53tiHtVm"
atoken="3444443115-fK0aKx79XpYonTyHmi1RLJmxPgzCYXHYjy509zd"
asecret="6DPyDerJOAPND45AP6SMOMAfYLIJX6DBsaRPQjMHIlfrS"

class twittertokafka(StreamListener):

    def __init__(self):
        self.kafka =  KafkaClient("localhost:9092")
        self.producer = SimpleProducer(self.kafka)

    def from_twitter(self,data):
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, twittertokafka())
        twitterStream.filter(track=['Hillary Clinton', '@hillaryclinton', '@ClintonNews', '@HRClinton', '@voteHillary2016', '@AllThingsHill', '@hillaryRussia', '@danmericaCNN', '@KThomasDC', '@anniekarni', '@AndrewStilesUSA', '@Madam_President', '@hillarynews1', '@FaithVotersPAC', '@HillDawgClinton', '@ABCLiz', '@NICKWALSH', '#Hillary2016', '@HillaryIn2016', 'Bernie Sanders', '@SenSanders', '@BernieSanders', '@ajbends', '@Bobby_Budds', '@Sanders4Potus', '@VoteBernie2016', 'Jeb Bush', '@JebBush', '@TeamJebBush', '@EliStokols', '@TomBeaumont', '@JBushNews', '@JBushNews', '@jebbushnews', '@VoteJeb', '@Bush', '@r2rusa', '@JebBushforPres', '@JebHillary2016', 'Donald Trump', '@realDonaldTrump', '@Writeintrump', '@Vote_For_Trump', '@NoahGrayCNN', '@DanScavino', 'John Kasich', '@JohnKasich', '@JohnKasichNews', '@TeamJohnKasich', '@GovernorKasich', 'Marco Rubio', '@marcorubio', '@TeamMarco', '@PoliticsTBTimes', '@MarcoRubioNews', 'Scott Walker', '@ScottWalker', '@GovWalker', '@wpjenna', '@ScottWalkerHQ'])

    def to_kafka(self, data):
        print(data)
        self.producer.send_messages("test", data)
        return(True)

    def on_error(self, status):
        print status



if __name__ == "__main__":
    tk=twittertokafka()
    twittertokafka.to_kafka()
    twittertokafka.from_twitter()

