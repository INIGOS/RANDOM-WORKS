from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey="PAIr18UAn0LbzrsCKB1n3wgfn"
csecret="5dxvF1lRkMqosxchKTSwghenSwoml3PWHxPeTTHRhVHyg0l1A9"
atoken="3444443115-ujP4KC14HKS4LB9VoNnz3wBN6jtJao0cDnzOLo4"
asecret="uqJfCgf8KWuD4ek8vGrh0LcKd0Z8xm0iebRN1CqOhrhoi"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())

twitterStream.filter(track=['hockey', 'cricket'])