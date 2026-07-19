#!/usr/bin/env python3
# Build 3 video blog posts (WP post HTML + schema) → payload PNG for browser upload.
import io, os, json, gzip, struct, zlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))

STYLE = '''<style>
.jlv{font-family:Inter,-apple-system,sans-serif;color:#141a2e;line-height:1.75;}
.jlv h2{font-family:'Barlow Condensed',Impact,sans-serif;text-transform:uppercase;letter-spacing:1.2px;color:#0d1155;font-size:30px;margin:36px 0 12px;}
.jlv .vid-wrap{position:relative;padding-top:56.25%;margin:22px 0;box-shadow:0 14px 44px -16px rgba(13,17,85,.25);}
.jlv .vid-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0;}
.jlv .tkbox{background:#f7f2e7;border-left:4px solid #38b6ff;padding:20px 24px;margin:24px 0;}
.jlv .tkbox b{color:#0d1155;}
.jlv .tkbox ul{margin:10px 0 0 18px;}
.jlv .tkbox li{margin:7px 0;}
.jlv details{border:1px solid #e5e8f2;background:#fff;margin:28px 0;}
.jlv details summary{cursor:pointer;padding:16px 20px;font-family:'Barlow Condensed',Impact,sans-serif;text-transform:uppercase;letter-spacing:1.4px;font-weight:700;color:#0d1155;background:#f5f7fc;font-size:19px;}
.jlv details .tr-body{padding:8px 24px 20px;}
.jlv details h4{color:#1795e0;text-transform:uppercase;letter-spacing:1px;font-size:14px;margin:18px 0 6px;}
.jlv .cta-line{background:#0d1155;color:#fff;padding:22px 26px;margin:30px 0 6px;}
.jlv .cta-line a{color:#38b6ff;font-weight:700;text-decoration:none;}
.jlv .yt-sub{display:inline-block;background:#c0392b;color:#fff;font-weight:700;padding:10px 18px;text-decoration:none;margin-top:8px;}
</style>'''

def video_embed(vid):
    return ('<div class="vid-wrap"><iframe src="https://www.youtube.com/embed/%s" title="Joga Labs video" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" '
            'allowfullscreen loading="lazy"></iframe></div>' % vid)

def schema(vid, name, desc, up):
    return ('<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "VideoObject",
        "name": name, "description": desc,
        "thumbnailUrl": "https://img.youtube.com/vi/%s/hqdefault.jpg" % vid,
        "uploadDate": up, "embedUrl": "https://www.youtube.com/embed/%s" % vid,
        "contentUrl": "https://www.youtube.com/watch?v=%s" % vid,
        "publisher": {"@type": "Organization", "name": "Joga Labs",
                      "logo": {"@type": "ImageObject", "url": "https://jogalab.com/wp-content/uploads/2025/10/JOGALABS-PlayMore-e1761587146210.png"}},
        "author": {"@type": "Person", "name": "Roberto Avey"}}, ensure_ascii=False) + '</script>')

CTA = ('<div class="cta-line"><b>Watch more soccer breakdowns.</b> New videos on tactics, leadership, futsal development '
       'and Brazilian football — <a href="https://www.youtube.com/@jogalabs?sub_confirmation=1" target="_blank" rel="noopener">subscribe to Joga Labs on YouTube</a>. '
       'Want your player training this way? <a href="/futsal-teams/">Join our competitive futsal club in Keller, TX</a>.</div>')

posts = []

# ================= POST 1: FUTSAL =================
p1_desc = "Coach Roberto Avey breaks down 11 ways futsal creates better outdoor soccer players — keeper reactions, quick shots, composure, movement and more. Full transcript included."
p1 = STYLE + '<div class="jlv">' + schema('I2FljcfwqT4', "Why Futsal Creates Better Outdoor Soccer Players (11 Reasons)", p1_desc, "2026-01-07") + '''
<p>Why do so many of the world's best players — Messi, Neymar, Ronaldinho, R9 — come from a futsal background? In this video, Coach Roberto Avey (founder of Joga Labs, a competitive youth futsal club in Keller, TX, and a lifelong futsal player from Campinas, Brazil) lays out eleven specific ways futsal builds better outdoor soccer players, from goalkeepers to strikers.</p>
''' + video_embed('I2FljcfwqT4') + '''
<div class="tkbox"><b>Key takeaways</b>
<ul>
<li><b>Keepers develop fastest in futsal</b> — 20–30 shots faced per game builds reactions, timing and confidence, plus the foot skills the modern game demands.</li>
<li><b>Defenders become technical</b> — man-to-man marking and tight-space play turn defenders into the skilled, ball-playing type today's game requires.</li>
<li><b>Attackers get quicker</b> — quick shots, faster decisions, and real composure under constant pressure.</li>
<li><b>The game teaches geometry</b> — triangles, one-twos, overloads and constant movement; there's nowhere to hide on a futsal court.</li>
<li><b>Modern football mimics futsal</b> — tight quarters, playing out of the back, tactical possession. Barcelona's tiki-taka era was arguably built on a futsal base.</li>
</ul></div>

<h2>The 11 Reasons</h2>
<p><b>1. Keeper development.</b> In a single futsal game a goalkeeper faces 20 to 30 shots and makes numerous saves — improving reaction, timing and confidence at a rate the outdoor game simply can't match.</p>
<p><b>2. Keeper foot skills.</b> The modern game requires keepers who are proficient with the ball — many managers, like Pep Guardiola, build their entire strategy from the back. Futsal makes keepers confident and precise with their feet.</p>
<p><b>3. Better defenders.</b> Long gone are the days when defenders just intimidated and kicked the ball out. Today's defenders are as technical as midfielders — and futsal builds those skills plus man-to-man marking, a core part of the futsal game.</p>
<p><b>4. Quick shots.</b> Ever coached kids who take a big wind-up and several seconds to set their body before shooting? Futsal demands instant shots and reactions — it fixes this.</p>
<p><b>5. Decision-making.</b> Futsal is fast. There's no time to sit and think, so your reaction and thought process sharpen — and that carries straight into the outdoor game.</p>
<p><b>6. Skill.</b> Futsal is known for producing some of the best players in the world: Neymar, Messi, Ronaldinho and R9 all came from a futsal base. And it's not freestyle trickery — futsal creates extremely technical players who can break down a defense and get the shot off.</p>
<p><b>7. Intensity.</b> Futsal is a game of sprints and counterattacks. It trains intense play with good decisions at speed.</p>
<p><b>8. Composure.</b> "This player needs more composure on the ball" is the most common note coaches give. In futsal you always have opponents on you, pushing you — you get used to pressure and learn to react. When you return outdoors, the intensity drops but the composure is everlasting.</p>
<p><b>9. Physicality.</b> You learn to shield and protect the ball — especially at the pivô position, which has to hold the ball up and bring the team up the court.</p>
<p><b>10. Movement and triangles.</b> Futsal teaches the geometry of the game — overloads, one-twos, constant rotation. Passing has to be perfect and you must move to receive. Mistakes are obvious to everyone, which is exactly why players develop so quickly.</p>
<p><b>11. The perfect foundation for the modern game.</b> Modern football has moved toward futsal: constant sprints, tight quarters, playing from the back with technical keepers and defenders, tactical possession instead of booting it to the corner flag. Barcelona's tiki-taka era — Iniesta, Xavi, Messi, Dani Alves rotating through triangles and one-twos — was arguably built on futsal.</p>
''' + CTA + '''
<details><summary>Full Video Transcript</summary><div class="tr-body">
<h4>Intro</h4>
<p>It's called the beautiful game for a reason. Nothing beats playing the game in its original state — outside, 11 versus 11, on the crisp, pristine, freshly cut grass of a pitch. However, the indoor sport of futsal is just as enjoyable as outdoor soccer and offers a wide range of benefits for both beginners and advanced players. Yours truly played futsal growing up, and it eventually became my main sport. At a place called Taquaral, I'd play pickup almost every weekend. I'd run a few laps around the park, then play games until blisters formed on my feet, ending the day with an água de coco. Anyways, enough about me — here are 11 ways futsal can improve your soccer skills and better prepare you for the next level.</p>
<h4>Goalkeeper Involvement</h4>
<p>Number one: keeper development. When you speak about development, futsal can help the keeper with reactions and the quantity of shots. In a single futsal game, the goalkeeper will face 20 to 30 shots and make numerous saves. This will help improve reaction, timing, and confidence.</p>
<h4>Goalkeeper Foot Skills</h4>
<p>Number two: keeper foot skills. The modern game requires keepers to be proficient with the ball — so much so that some managers, like Pep Guardiola, start their entire game strategy from the back. Futsal is a game that helps keepers become confident and precise with the ball at their feet. If you are a keeper, then futsal is the perfect foundational sport to improve in this area.</p>
<h4>Defenders in Futsal</h4>
<p>Number three: improving defenders. Long are the days when defenders were there to intimidate and kick the ball out. These days, defenders are just as skilled and technically sound as many midfielders. Some may even argue that the defenders of today's age might have been CDMs back 20 years ago. Futsal helps defenders with technical skills as well as marking players, since marking man-to-man and following your man is a major part of the futsal game.</p>
<h4>Quick Shots &amp; Finishing</h4>
<p>Number four: quick shots. Have you ever coached kids and noticed they do this big wind-up to prepare for shooting? They take several seconds to adjust their body and try to get the ball perfect before a shot. Well, futsal is a game where quick shots and reactions are necessary. Futsal will fix this issue.</p>
<h4>Faster Decision-Making</h4>
<p>Number five: decision-making. Futsal is a quick game. You don't have much time to sit and think. Your reaction and thought process will improve — and this will benefit you when you go to the outdoor game.</p>
<h4>Skill Development</h4>
<p>Number six: skill. Futsal is known for creating some of the best players in the world. Neymar, Messi, Ronaldinho, and R9 all came from a futsal base. But don't get this wrong — this isn't freestyle trickery. Futsal helps create extremely technical players with the ability to break down defenses and get the shot off. Futsal is not a freestyle trickery game, even though sometimes fancy tricks are used.</p>
<h4>Game Intensity</h4>
<p>Number seven: intensity. Futsal is a game of sprints and counterattack play. If you want to improve on intense play with good decision-making and counterattacks, then futsal will help.</p>
<h4>Composure Under Pressure</h4>
<p>Number eight: composure. I hear this a lot as a coach: "The player needs more composure with the ball. They get anxiety, make mistakes when they have the ball." A player gets composure when they get used to players near them, and they begin to be more confident. In futsal, you will have players on you, pushing you. This will help with composure. You will get used to the pressure from players forcing you to react. When you go to outdoor soccer, the intensity will be less, but your composure will be everlasting.</p>
<h4>Physicality in Futsal</h4>
<p>Number nine: physicality. You learn to shield and protect the ball — especially as a pivô. The pivô position, or top attacking player, will need to hold the ball and help bring the team up the court. All players will learn to shield and protect the ball. This will benefit them when moving to outdoor soccer.</p>
<h4>Movement, Triangles &amp; Spacing</h4>
<p>Number ten: movement and triangles. Futsal teaches the geometry of the game — movement, overloading sides, one-twos. There's nowhere to hide on a futsal court. The passing has to be perfect. You must move to receive the ball. If you make a mistake on the court, it will be blatantly obvious to you and everyone else. This helps players develop quickly.</p>
<h4>Modern Football &amp; Futsal</h4>
<p>Futsal is the perfect foundational sport for outdoor soccer. Let me explain. Modern football has actually transitioned to more similarities with a futsal game than it had 20 years ago. The modern outdoor game is physically demanding, with constant sprints giving less space and time for the players to think. They operate in tight quarters and must have better passing than in the past. They do lots of triangles and play from the back with keepers and defenders who are technically sound with the ball. The modern outdoor game has become a tactical possession sport that mimics futsal. Long gone are the days of booting the ball to the corner flag.</p>
<h4>Barcelona &amp; Tiki-Taka</h4>
<p>I'd even argue that futsal was the basis during the era of Barcelona's tiki-taka football. Iniesta, Xavi, Messi, and Dani Alves would move doing triangles, rotating, doing one-twos, and holding the ball, waiting for the perfect time to quickly attack and get the shot off.</p>
<p>What say you? Did I miss something? Let me know in the comments below.</p>
<p><em>Transcript lightly edited from YouTube captions for readability.</em></p>
</div></details>
</div>'''
posts.append({
 'slug': 'why-futsal-creates-better-soccer-players',
 'title': "Why Futsal Creates Better Outdoor Soccer Players — 11 Reasons (Video + Transcript)",
 'content': p1,
 'yoast_title': "Why Futsal Creates Better Soccer Players: 11 Reasons (Video) | Joga Labs",
 'yoast_desc': "Coach Roberto Avey breaks down 11 ways futsal develops better outdoor soccer players — keeper reactions, quick decisions, composure & more. Full transcript.",
 'tags': ['futsal', 'player development', 'soccer training', 'futsal vs soccer'],
})

# ================= POST 2: BRAZIL =================
p2_desc = "What's wrong with Brazil's national team? Coach Roberto Avey analyzes clips from Brazilian journalists and ex-players on the CBF, empty stadiums, the Ancelotti saga, and R9's run for CBF president."
p2 = STYLE + '<div class="jlv">' + schema('VdEe1E8CLj8', "What's Wrong With Brazil's National Soccer Team - Part 1", p2_desc, "2024-12-21") + '''
<p>Why has the most successful national team in World Cup history looked so ordinary for a decade? In Part 1 of this series, Coach Roberto Avey — who grew up playing in Campinas, Brazil — breaks down clips from Brazilian journalists, pundits and ex-players to examine what's really going on inside the Seleção and the CBF (Brazilian Football Federation). It ends with a surprise: the campaign of a very famous World Cup winner to fix it all.</p>
''' + video_embed('VdEe1E8CLj8') + '''
<div class="tkbox"><b>Key takeaways</b>
<ul>
<li><b>The decline is real but not unprecedented</b> — even the 2002 champions and the 1994 team struggled through qualifying (Romário rescued the '94 side in the final qualifier).</li>
<li><b>The problems start at the top</b> — CBF power plays, back-room deals to hold power until 2034, ticket prices near half a month's minimum wage, and empty stadiums.</li>
<li><b>The league works against the national team</b> — Brazil semi-ignores FIFA dates, shoving weekend fixtures into midweek and overloading players.</li>
<li><b>The Ancelotti handshake saga</b> — no contract, a year and a half of interim managers, then nothing. Why would an elite foreign manager walk into that disorder?</li>
<li><b>The hope: R9</b> — Ronaldo's run for CBF president, and why a football man beats a career bureaucrat.</li>
</ul></div>

<h2>A decade of decline</h2>
<p>The video opens with the question every Brazilian fan keeps asking: why has the Seleção been so poor for roughly ten years? The first clips break down the final 2024 World Cup qualifier of the year against Uruguay — a flat 1–1 draw that was hard to watch, let alone cheer. The pundits add historical perspective: Brazil has had rough qualifying campaigns before, including the 2002 team that went on to win it all, and the 1994 side that needed two Romário goals in the final qualifier just to reach the World Cup.</p>
<h2>The federation problem</h2>
<p>From there, the analysis turns to the CBF. There's little direction, little hope, and no cohesion around the team — and at the top sits a president more focused on power plays than football. Ticket prices for national team games were raised to roughly R$600 — nearly half a month's minimum wage in Brazil — at year-end, and the stadium sat empty. As Roberto puts it: you're not watching a Ronaldinho or a Neymar out there, so why would fans pay that to watch mediocrity?</p>
<h2>Why elite managers won't come</h2>
<p>Could a Guardiola or an Ancelotti fix the Seleção? The clips make a sharp point: any foreign manager will do due diligence — and they'll find a federation president cutting deals to stay in power until 2034, a domestic league that only pretends to respect FIFA dates (weekend games get pushed to midweek, overloading players and sabotaging call-ups), and Copa América logistics so bad the team was stranded in the United States without flights home. Five-time world champions, run that poorly. The Ancelotti chapter says it all: a handshake agreement with no contract, a year and a half of interim managers — Ramon Menezes, Fernando Diniz — and then Ancelotti walked away.</p>
<h2>The big reveal: R9 for CBF president</h2>
<p>The video closes with Ronaldo — R9, the original — announcing his campaign for CBF president. His stated mission: rescue Brazilian football, restore the confidence and respect Brazil once commanded worldwide, and elevate the leagues, players and managers globally. Roberto's case for him: playing experience at the highest level, real business experience, and worldly wisdom — versus a lifelong desk bureaucrat. As in the corporate world, when leaders who never worked the floor take over, the business suffers. It's time for someone who knows the industry from the ground up.</p>
''' + CTA + '''
<details><summary>Full Video Transcript (condensed)</summary><div class="tr-body">
<p>So what's going on with the Brazilian national football team? Why have they been so poor the last several years — I would say the last 10 years, to be exact? I get this question a lot, from friends I play with, from kids I coach and train, and it's hard to understand why there's been such a drastic decline. Today I'm going to put together a few clips from Brazil — from journalists, pundits, as well as ex-players. We'll analyze them, and at the end I have a special surprise about an older World Cup-winning player, a very famous guy. This is going to be a series — we have a lot to talk about.</p>
<p><b>On the Uruguay game:</b> First off, they're discussing the final game of 2024 against Uruguay in Brazil for World Cup qualifying. It was a 1–1 tie — a pretty slouchy game, hard to watch, hard to stand up and cheer. They also point out there have been other difficult campaigns: even the 2002 World Cup-winning team hardly qualified, and in 1994 Brazil had a lot of problems qualifying as well — Romário had to come in and score two goals in the final qualifying game to advance them to the World Cup.</p>
<p><b>On the Seleção's direction:</b> There's very little direction and very little hope. The cohesiveness is not there whatsoever. All of that is hurting the play — as well as the CBF president, who has this kind of inferiority complex where he tries to show he's the most powerful, the man in charge, doing all these political things. We have really good players, but they're not the lead player on their teams in Europe. There's Vini Jr — he shares that responsibility with other players at Real Madrid — but he doesn't play very well for the Seleção. Maybe it's not fair to expect him to play like a Neymar, a Ronaldinho, or an R9 — but it is proper to have those expectations. If he wants the Ballon d'Or, he needs to play better for the Brazilian national team. There's absolutely no doubt about that in my mind.</p>
<p><b>On the empty stadium:</b> The stadium was empty and it was extremely expensive — one of those power plays by the CBF president. He raised the prices and people don't go. Why would they? You're not watching a Ronaldinho, you're not watching a Neymar — you're watching a team playing mediocre football. Tickets went up to around R$600 at the end of the year — when the minimum wage is about R$1,400 in Brazil, that's nearly half a month's salary just to watch the Seleção.</p>
<p><b>On hiring a foreign manager:</b> They discuss bringing in a manager from overseas — a Pep Guardiola, a Carlo Ancelotti. But here's the good point: say we invite a foreign manager. They're going to do their research, talk to friends and past Brazilian players they've managed. They'll see the current CBF president doing power plays and back-room deals to stay in power for another 10 years, until 2034. Then they'll hear the Brazilian league doesn't respect the FIFA dates — during international windows, leagues in England, Spain, Italy and the USA stop for about 10 days; in Brazil they semi-stop, pushing weekend games to midweek. If you're the national team coach and want to call up a player from the Brazilian league, it becomes very difficult — the player is overloaded. Then, logistically: during Copa América, Brazil didn't have flights home and had to stay an extra day in the United States because someone mismanaged the travel. Five-time world champions — the team with probably the most notoriety in the world — and it's that unorganized. It's hard to bring in a Guardiola or an Ancelotti and expect them to want to join complete disorder.</p>
<p><b>The Ancelotti saga:</b> The CBF president did a handshake deal with Carlo Ancelotti, the Real Madrid manager, to take over the Seleção. For a year and a half we had interim managers — Ramon Menezes, Fernando Diniz — and it was poorly managed. Nothing was written on paper, there were no contracts. After a year and some months, Ancelotti said: I don't want to be part of this.</p>
<p><b>The reveal — R9:</b> Who's going to be the next CBF president? R9. Ronaldo — the original, the real one. The gods of football blessed Ronaldo with speed, ability, agility, force, and wisdom in the sport. Why does he want to become president of the Brazilian Federation? He said it clearly: he wants to rescue football in Brazil, bring back the confidence and respect Brazil had throughout the world, and elevate the leagues, the players and the managers globally. I feel he has the capacity to do it. He has the playing experience, he's been in business for a while, he's not a lifelong bureaucrat or politician. He's someone who already has that confidence and worldly wisdom — he's worked and played all over the world. Being a leader takes sternness, confidence, and most of all critical thinking. The current president is in a constant power-play struggle. We've all been in situations with that sort of character — a lifelong person behind the desk who never applied anything, suddenly becomes a leader, is supposed to transform the business, and two or three years later there are layoffs everywhere. It's time to get someone who actually worked in the industry from the ground up, knows the ins and outs, and isn't there to do power plays.</p>
<p>I'm happy R9 is doing this — I think he has the capacity. I'd love to hear what you have to say: put comments below in English, Portuguese, Spanish, Italian — whatever you feel. Like and subscribe: I'm going to do several more of these videos about the CBF, the Seleção, Vini Jr and other players. There's a lot to come. Talk to you soon — 'tá bom?</p>
<p><em>Transcript lightly edited from YouTube captions for readability; Brazilian names and terms corrected.</em></p>
</div></details>
</div>'''
posts.append({
 'slug': 'whats-wrong-with-brazil-national-team-part-1',
 'title': "What's Wrong With Brazil's National Soccer Team? — Part 1 (Video + Transcript)",
 'content': p2,
 'yoast_title': "What's Wrong With Brazil's National Team? Part 1 (Video) | Joga Labs",
 'yoast_desc': "Coach Roberto Avey analyzes Brazil's decade of decline: CBF power plays, empty stadiums, the Ancelotti saga & R9's run for president. Video + transcript.",
 'tags': ['brazil national team', 'seleção', 'CBF', 'ronaldo r9', 'brazilian football'],
})

# ================= POST 3: AMORIM =================
p3_desc = "Ruben Amorim called Manchester United 'maybe the worst team in history.' Coach Roberto Avey breaks down what his press conference teaches about leading a struggling team — in football and in business."
p3 = STYLE + '<div class="jlv">' + schema('Nlx8qWqa1zY', "Amorim Press Conference - How To Be A Leader in Tough Situations Manchester United", p3_desc, "2025-01-28") + '''
<p>"We are being the worst team maybe in the history of Manchester United." When Ruben Amorim said that in a live press conference, it made every headline in world football. In this video, Coach Roberto Avey breaks down the clips and asks the bigger question: is that how a leader takes over a struggling team? The lessons apply far beyond football — to business, coaching, and any new leadership role.</p>
''' + video_embed('Nlx8qWqa1zY') + '''
<div class="tkbox"><b>Leadership lessons from the breakdown</b>
<ul>
<li><b>Never badmouth your team in public.</b> Say what you need behind closed doors — the locker room, the training pitch — never in front of the world.</li>
<li><b>The new leader owns part of the problem.</b> If the team performs worse after you arrive, you're a big percentage of the issue.</li>
<li><b>Adapt your system to your people.</b> You can't run "your style" at 100% with players who don't fit it — run it at 50% until you have your people.</li>
<li><b>Don't be stubborn when you can see the iceberg.</b> Roll with the punches, move roles around, pivot.</li>
<li><b>Leadership needs training.</b> Football is a business — press and people skills don't come automatically from 20 years of kicking a ball.</li>
</ul></div>

<h2>"Don't hold back, buddy"</h2>
<p>The breakdown opens with the quote itself. Roberto's reaction: whoa — is that how you feel about your team? Imagine a new leader in a company walking in and announcing "my team sucks." You will get nothing out of your players — or your employees — after that. A new coach losing more games than the last coach is, in Roberto's words, a huge part of the problem himself: the players don't want you yet, and you can't impose your system at 100% before your own players arrive.</p>
<h2>The headlines write themselves</h2>
<p>"You want headlines? Here are your headlines: MY TEAM SUCKS." Roberto asks whether Amorim has had any press training at all — because football is a business, just like the one you walk into every morning. Reaching a leadership position requires leadership skills, no matter how long you've been on the pitch. And if you're going to be cheeky off the cuff, you'd better back it up with results.</p>
<h2>What Amorim got right</h2>
<p>To be fair, the clips also show Amorim owning the moment: "Everybody here is underperforming... it's unacceptable to lose so many games for any club in the Premier League — imagine Manchester United... we have to continue, there is no other way. We need to suffer." He admits he knew installing a completely new idea mid-season would be hard. The honesty is real — the delivery is the problem.</p>
<h2>If you lead a new team, listen</h2>
<p>Roberto closes with the playbook for anyone taking over a struggling team: never badmouth your people, publicly or otherwise. Get the most out of the team you have. Change responsibilities and roles; move people around. Don't be hard-headed, don't be stubborn — roll with the punches and pivot. And a wink to finish: "Amorim, we're thankful you're here — you're definitely better than the last guy. Then again, anybody could have been better than the last guy."</p>
''' + CTA + '''
<details><summary>Full Video Transcript</summary><div class="tr-body">
<p><b>Amorim (clip):</b> "So, um, we are being the worst team maybe in the history of Manchester United."</p>
<p><b>Roberto:</b> Whoa, whoa, whoa buddy — don't hold back! Is that how you feel about your team, about your players? Is that what we're getting when a new coach — that is losing more than the last coach — comes in? I have full knowledge of that: you're 60% of the problem. They were playing worse, you knew what you were coming into, you have players that don't want you. You can't play Amorim-style football 100% — you've got to do Amorim-style football 50% until you get your new players in.</p>
<p><b>Amorim (clip):</b> "That's it. I'm not going to change, no matter what."</p>
<p><b>Roberto:</b> Is this the moment to be hard-headed? You see the iceberg ahead of you and you're going to drive right into it, Mr. Titanic? What's going on?</p>
<p><b>Amorim (clip):</b> "I know we can succeed, but we need to survive this moment, because I'm not naive and I know that we need to survive now... we are being the worst team maybe in history of Manchester United."</p>
<p><b>Roberto:</b> The worst team in the history of Manchester United — whoa, let us know how you really feel! Is that how a leader comes into a new gig? Can you imagine in corporate, or in your own business, somebody comes in: "my team sucks"? Amorim, you're a big part of the issue, man. You're not going to get anything out of your players by saying they suck. You can say whatever you want to them behind closed doors, in the locker room, on the training pitch — but in front of everyone else, you can't say that type of stuff. I know you want headlines... well, here you go, here are your headlines: MY TEAM SUCKS. Has this guy had any press training? This is insane. Listen — football is a business, just like corporate, just like your work every morning. You have to have had some type of training when you get to a leadership position. I don't care if you've been kicking a ball around for the last 20 years — you have to have those leadership skills. It's incredible that he's just coming out and blatantly saying this stuff. You can be a little bit cheeky, off the cuff — that's fine. But if you're going to be off the cuff and cheeky, you'd better demonstrate it on the pitch.</p>
<p><b>Amorim (clip):</b> "Everybody here is underperforming. No matter the circumstances, we are underperforming and we have to accept that. It's unacceptable to lose so many games for any club in the Premier League — imagine Manchester United. So it's a really hard moment, but we have to continue. There is no other way. We need to suffer and continue. I knew it was going to be hard to put a completely new idea in this moment, but when you lose games you don't have that luck. To win three games in a row is becoming really hard. That's why I'm telling you we are going to suffer — because I will continue to do the same."</p>
<p><b>Roberto:</b> If you're a leader, this is a great example of what NOT to do when you're coming into a difficult new position. Don't badmouth your team — ever. Try to get the most out of the players, out of your team members. Change responsibilities and roles, move people around. Don't be hard-headed. Do not be stubborn. Roll with the punches — pivot, change. Amorim, we're thankful you're here at Manchester United. You're definitely better than the last guy... well, I think anybody could have been better than the last guy.</p>
<p><em>Transcript lightly edited from YouTube captions for readability.</em></p>
</div></details>
</div>'''
posts.append({
 'slug': 'amorim-press-conference-leadership-lessons',
 'title': "Amorim's “Worst Team in History” Press Conference — Leadership Lessons (Video + Transcript)",
 'content': p3,
 'yoast_title': "Amorim Press Conference: Leadership Lessons (Video) | Joga Labs",
 'yoast_desc': "Amorim called Man United 'the worst team in history.' Coach Roberto Avey breaks down what it teaches about leading a struggling team. Video + transcript.",
 'tags': ['ruben amorim', 'manchester united', 'leadership', 'press conference'],
})

payload = {'category': {'name': 'Video Blog', 'slug': 'video-blog',
                        'description': 'Soccer videos from Coach Roberto Avey — tactics, leadership, futsal development and Brazilian football, every video fully transcribed.'},
           'posts': posts}
raw = gzip.compress(json.dumps(payload, ensure_ascii=False).encode('utf-8'))

def chunk(typ, data):
    return struct.pack('>I', len(data)) + typ + data + struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff)
png = (b'\x89PNG\r\n\x1a\n'
       + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
       + chunk(b'IDAT', zlib.compress(b'\x00\x00\x00\x00'))
       + chunk(b'IEND', b''))
io.open('jl-videoposts-data.png', 'wb').write(png + b'JLDATA' + raw)
print('payload gz bytes:', len(raw), '| posts:', [p['slug'] for p in posts])
