# -*- coding: utf-8 -*-

import requests
import json

cookies1 = {
	"cid":"2001072207",
	"portal_tid":"1471678585599-63567",
	"user":"MrZhigan",
	"password":"af2b2e5dd598b806128e408c5b7873ff7b7634b8",
	"no_remember":"0",
	"portal_data":"portal_tid=1471678585599-63567",
	"__utmt":"1",
	"__utma":"189530924.2098698103.1471678586.1472760504.1472810817.4",
	"__utmb":"189530924.1.10.1472810817",
	"__utmc":"189530924",
	"__utmz":"189530924.1471678586.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
	"_dc_gtm_UA-50308805-1":"1",
	"_dc_gtm_UA-1897727-9":"1",
	"sid":"0%3A4c655c630b21",
	"ref1720916":"start",
	"_ga":"GA1.2.2098698103.1471678586",
	"__utma":"236281090.2098698103.1471678586.1472760508.1472810823.4",
	"__utmb":"236281090.5.10.1472810823",
	"__utmc":"236281090",
	"__utmz":"236281090.1472810823.4.4.utmcsr=voyna-plemyon.ru|utmccn=(referral)|utmcmd=referral|utmcct=/",
	"global_village_id":"5562",
	"mobile":"0"
}

cookies2 = {
	"cid":"2001072207",
	"portal_tid":"1471678585599-63567",
	"user":"MrZhigan",
	"password":"af2b2e5dd598b806128e408c5b7873ff7b7634b8",
	"no_remember":"0",
	"portal_data":"portal_tid=1471678585599-63567",
	"__utma":"189530924.2098698103.1471678586.1472760504.1472810817.4",
	"__utmb":"189530924.1.10.1472810817",
	"__utmc":"189530924",
	"__utmz":"189530924.1471678586.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
	"sid":"0%3A4c655c630b21",
	"ref1720916":"start",
	"_ga":"GA1.2.2098698103.1471678586",
	"__utmt":"1",
	"global_village_id":"5562",
	"mobile":"0",
	"__utma":"236281090.2098698103.1471678586.1472760508.1472810823.4",
	"__utmb":"236281090.14.10.1472810823",
	"__utmc":"236281090",
	"__utmz":"236281090.1472810823.4.4.utmcsr=voyna-plemyon.ru|utmccn=(referral)|utmcmd=referral|utmcct=/"
}

def step(url, data, cookies):
	return requests.post(url, data=data, cookies=cookies).text.encode('utf8')


r1 = step(
	url = "https://ru42.voyna-plemyon.ru/game.php?village=5562&screen=place&try=confirm&",
	data = {
		u"69fb9bc7a0e3f46c598bbe":u"d2e6506969fb9b",
		u"template_id":u"",
		u"source_village":u"5562",
		u"spear":u"8",
		u"sword":u"8",
		u"axe":u"",
		u"archer":u"",
		u"spy":u"",
		u"light":u"",
		u"marcher":u"",
		u"heavy":u"",
		u"ram":u"",
		u"catapult":u"",
		u"knight":u"",
		u"snob":u"",
		u"x":u"447",
		u"y":u"553",
		u"target_type":u"coord",
		u"input" :u"447|553",
		u"attack":u"Атака",
	}, cookies=cookies1)

r2 = step(url="https://ru42.voyna-plemyon.ru/game.php?village=5562&screen=place&action=command&h=d2873780",
	data={
		"attack":"true",
		"ch":"5ba9346ffc218b31ce0163393b5f4463c919f232",
		"x":"446",
		"y":"548",
		"source_village":"5562",
		"action_id":"708505",
		"attack_name":"",
		"spear":"8",
		"sword":"8",
		"axe":"0",
		"archer":"0",
		"spy":"0",
		"light":"0",
		"marcher":"0",
		"heavy":"0",
		"ram":"0",
		"catapult":"0",
		"knight":"0",
		"snob":"0",
		"building":"main",
	}, cookies=cookies2)

print requests.post(url="https://ru42.voyna-plemyon.ru/game.php?village=5562&screen=place", cookies=cookies1).text.encode('utf8')

open('resp1.html', 'w').write(r1)
open('resp2.html', 'w').write(r2)

# print requests.post(url,data=data, cookies=cookies).text.encode('utf8')

