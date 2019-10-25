import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

cfg = {
    "consumer_key"        : "Insert Consumer Key here",
    "consumer_secret"     : "Insert Consumer Secret here",
    "access_token"        : "Insert Access token here",
    "access_token_secret" : "Insert Access token secret here"
    }


API = get_api(cfg)
