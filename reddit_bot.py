import praw
import time
import json
import sys
import urllib.request
from urllib.request import Request, urlopen
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from dhooks import Webhook
from requests import Session
from dhooks import Embed


embed = Embed(
    description='New Post',
    color=0x5CDBF0,
    timestamp='now'  # sets the timestamp to current time
    )

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}


reddit = praw.Reddit(client_id="i_2KaQSuTnH8Ng",
                     client_secret="kbSmradE8grBrfcTVE8kyXBx_jk",
                     password="Unit5007",
                     user_agent="minimalBot",
                     username="Snekxs")
print("Logged In As",reddit.user.me())

subreddit = reddit.subreddit("minimal_setups")
count = 1

hook = Webhook('https://discord.com/api/webhooks/749354236311109662/QxLJSUqU3uFl4HBRLxYABqnh85skVAk252RrbAHkMEC522or6SuW-EXfaKJ-T5rR3kXs')
hook1 = Webhook('https://discord.com/api/webhooks/749816474746617956/8mw-F8VN7Ok3p2XSuC9PcnDCKbwq1Qmp1brDt0Jh5IBPKnyR1m6W3OwtjRuQLSwAutIV')




for submission in subreddit.top("month", limit=5):
    hook.send(f"https://reddit.com/{str(submission.permalink)}")
    print(f"https://reddit.com/{str(submission.permalink)}")
    print(f"https://reddit.com/user/{str(submission.author)}")


hook1.send(embed=embed)


for submission in subreddit.top("month", limit=5):
    url = str(submission.url)

    if url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        urllib.request.urlretrieve(url, f"image{count}.jpg")
        count += 1
        print("Done")

                
        if count == 6:
    
            break
        

for submission in subreddit.stream.submissions(skip_existing=True):
	imagerequests = requests.get(f"https://reddit.com/{str(submission.permalink)}.json", headers=headers).json()
	imageurl = imagerequests[0]["data"]["children"][0]["data"]["url"]
	print(imageurl)
	if "jpg" not in imageurl:
		embed = Embed(color=0x008080, timestamp='now')
		embed.set_title(title=str(submission.title), url=f"https://reddit.com{str(submission.permalink)}")
		embed.set_author(name="Minimal_Setups", url="https://www.reddit.com/r/Minimal_Setups/",icon_url="https://styles.redditmedia.com/t5_rtmbn/styles/communityIcon_7qjzvrk4fjp41.png")
		embed.add_field(name="Author",value=str(submission.author), inline=False)
		hook1.send(embed=embed)
	else:
		print("Image Found")
		embed = Embed(color=0x008080, timestamp='now')
		embed.set_title(title=str(submission.title), url=f"https://reddit.com{str(submission.permalink)}")
		embed.set_author(name="Minimal_Setups", url="https://www.reddit.com/r/Minimal_Setups/",icon_url="https://styles.redditmedia.com/t5_rtmbn/styles/communityIcon_7qjzvrk4fjp41.png")
		embed.add_field(name="Author",value=str(submission.author), inline=False)
		embed.set_image(imageurl)
		hook1.send(embed=embed)
    


