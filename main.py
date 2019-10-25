from API_Token import API
import Loader
import time

def TweetParser(tweets):
    for tweet in tweets:
        if tweet._json['full_text'][:2] != "RT":
        #By excluding tweets where the first two letters are RT
        #only non-retweets(i.e tweets written by user), are scraped
            maindict[tweet._json['id']] = tweet._json['full_text']
    Loader.TweetFileWriter(maindict)

def ratelimitcountchecker(count):
    if (count % 10) == 0:
        return ratelimit()
    else:
        return True

def Setup():
    print("Starting Tweet Scraper")
    count = 0
    ratelimitcheck = True
    PersonID = 704440164
    global maindict
    PersonInfo = {PersonID : {
        "oldmax_id"    : 0,
        "laststop_id" : 0
    }}
    print("Parsing account id:{}".format(PersonID))
    try:
        ParserInfo = Loader.ParserInfoReader()
        print("Successfully loaded information for account id:{}".format(PersonID))
    except:
        print("Couldn't load local information for account id:{}".format(PersonID))
        pass
    else:
        if PersonID in ParserInfo.keys():
            PersonInfo[PersonID]['oldmax_id'] = ParserInfo[PersonID]['oldmax_id']
            PersonInfo[PersonID]['laststop_id'] = ParserInfo[PersonID]['laststop_id']
    maindict = Loader.TweetFileReader()
    start = API.user_timeline(id = PersonID, count = 1,tweet_mode='extended')
    newmax_id = start[0]._json['id']
    oldmax_id = PersonInfo[PersonID]['oldmax_id']
    laststop = PersonInfo[PersonID]['laststop_id']
    if oldmax_id == 0:
        PersonInfo[PersonID]['oldmax_id'] = newmax_id
    while ratelimitcheck and laststop !=0:
        tweets = API.user_timeline(id=PersonID, count=100, tweet_mode='extended', max_id=newmax_id)
        if int(tweets[-1]._json['id']) < oldmax_id and int(tweets[0]._json['id']) < oldmax_id:
            PersonInfo[PersonID]['oldmax_id'] = start[0]._json['id']
            print("Successfully added new tweets to main file. Going to last stop")
            break
        #time.sleep(2)
        TweetParser(tweets)
        newmax_id = tweets[-1]._json['id']
        ratelimitcheck = ratelimitcountchecker(count)
        count+=1
        print("Added information to main file. Current count is at {}".format(count))
    print("Going from last stop(newest tweet would be last stop if profile is newly added to parser).")
    print("Will run until rate limit is reached")
    while ratelimitcheck:
        if laststop == 0:
            laststop = start[0]._json['id']
        #time.sleep(2)
        tweets = API.user_timeline(id = PersonID, count = 100,tweet_mode='extended',max_id=laststop)
        if tweets == []:
            print("Reached furthest tweet possible. Currently set at 3200th most recent tweet (this number includes retweets)")
            break;
        TweetParser(tweets)
        PersonInfo[PersonID]['laststop_id'] = laststop
        Loader.ParserInfoWriter(PersonInfo)
        laststop = tweets[-1]._json['id']
        ratelimitcheck = ratelimitcountchecker(count)
        count+=1
        print("Added information to main file. Current count is at {}".format(count))


def ratelimit():
    '''Returns amount of requests left before reaching limit set by API.
    Included to ensure scraper doesnt crash due to API limits'''
    ratelimit = API.rate_limit_status()
    LimitOnRateLimit = ratelimit['resources']['application']['/application/rate_limit_status']['remaining']
    LimitOnTimeline = ratelimit['resources']['statuses']['/statuses/user_timeline']['remaining']
    if LimitOnRateLimit > 5 and LimitOnTimeline > 10:
        return True
    else:
        print("Rate Limit reached")
        return False


if __name__ == "__main__":
    Setup()