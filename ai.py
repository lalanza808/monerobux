# -*- coding: utf-8 -*-
import requests
import sopel.module

@sopel.module.commands('gp2', 'ai')
def gp2(bot, trigger):
    # bot.say("bomb-on ruined it for everyone. thanks bomb-on")
    text = trigger.group(2)
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': text,
        },
        headers={'api-key': '34b2c164-0c2e-4896-90ab-98dd56eeb290'}
    )
    #bot.say(r.json())
    bot.say(r.json()['output'].split('\n\n')[0])
    bot.say(r.json()['output'].split('\n\n')[1])
    bot.say(r.json()['output'].split('\n\n')[2])
    #bot.say("full output at http://ai.wownero.com")
    #stringtowrite = r.json['output'].encode('utf8')
    #with open("/root/www/index.html", "w") as f:
    #    f.write(stringtowrite)
