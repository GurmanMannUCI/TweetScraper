import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

cfg = {
    "consumer_key"        : "MPnmQEm0ivbtr0pZebox2it3b",
    "consumer_secret"     : "JE62GeBPUfKqYYs0XmpxrJmcnOL3Os87vJ77I9DhbLCB1PtY7e",
    "access_token"        : "704440164-OZYM0Pzxc1Yky8BFYHCmWZSUjp9EoGPFdqawlL7k",
    "access_token_secret" : "MlutZuvbNt4fe1En904hPCAf2MAn66nCm1YUpOb6lMcOa"
    }


API = get_api(cfg)
