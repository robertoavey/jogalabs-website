#!/usr/bin/env python3
# Emit videoposts_bodies.json for build_video_v2.py
import io, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

P1_ART = '''<p class="rv">Why do so many of the world's best players &mdash; Messi, Neymar, Ronaldinho, R9 &mdash; come from a futsal background? Coach Roberto Avey, founder of Joga Labs and a lifelong futsal player from Campinas, Brazil, lays out eleven specific ways futsal builds better outdoor soccer players, from goalkeepers to strikers.</p>
<div class="tkbox rv"><b>Key takeaways</b>
<ul>
<li><b>Keepers develop fastest in futsal</b> &mdash; 20&ndash;30 shots faced per game builds reactions, timing and confidence, plus the foot skills the modern game demands.</li>
<li><b>Defenders become technical</b> &mdash; man-to-man marking and tight-space play create the ball-playing defenders today's game requires.</li>
<li><b>Attackers get quicker</b> &mdash; quick shots, faster decisions, and real composure under constant pressure.</li>
<li><b>The game teaches geometry</b> &mdash; triangles, one-twos, overloads and constant movement; there's nowhere to hide on a futsal court.</li>
<li><b>Modern football mimics futsal</b> &mdash; tight quarters, playing out of the back, tactical possession. Barcelona's tiki-taka era was arguably built on a futsal base.</li>
</ul></div>
<h2 class="rv">The 11 reasons</h2>
<p><b>1. Keeper development.</b> In a single futsal game a goalkeeper faces 20 to 30 shots and makes numerous saves &mdash; improving reaction, timing and confidence at a rate the outdoor game can't match.</p>
<p><b>2. Keeper foot skills.</b> The modern game requires keepers who are proficient with the ball &mdash; managers like Pep Guardiola build their entire strategy from the back. Futsal makes keepers confident and precise with their feet.</p>
<p><b>3. Better defenders.</b> Today's defenders are as technical as midfielders &mdash; futsal builds those skills plus man-to-man marking, a core part of the game.</p>
<p><b>4. Quick shots.</b> No more big wind-ups and slow set-ups before shooting &mdash; futsal demands instant shots and reactions.</p>
<p><b>5. Decision-making.</b> Futsal is fast. There's no time to sit and think, so your reaction and thought process sharpen &mdash; and it carries straight outdoors.</p>
<p><b>6. Skill.</b> Neymar, Messi, Ronaldinho and R9 all came from a futsal base &mdash; and it's not freestyle trickery. Futsal creates technical players who break down defenses and get the shot off.</p>
<p><b>7. Intensity.</b> A game of sprints and counterattacks &mdash; it trains intense play with good decisions at speed.</p>
<p><b>8. Composure.</b> The most common coaching note there is. In futsal you always have opponents on you &mdash; you get used to pressure. Outdoors the intensity drops, but the composure is everlasting.</p>
<p><b>9. Physicality.</b> You learn to shield and protect the ball &mdash; especially at the piv&ocirc;, holding the ball up to bring the team up the court.</p>
<p><b>10. Movement and triangles.</b> The geometry of the game: overloads, one-twos, constant rotation. Passing must be perfect and mistakes are obvious &mdash; which is exactly why players develop so fast.</p>
<p><b>11. The perfect foundation for the modern game.</b> Modern football has moved toward futsal &mdash; constant sprints, tight quarters, playing from the back, tactical possession. Barcelona's tiki-taka era &mdash; Iniesta, Xavi, Messi, Dani Alves &mdash; was arguably built on futsal.</p>'''

P1_TR = '''<details class="rv"><summary>Full Video Transcript</summary><div class="tr-body">
<h4>Intro</h4>
<p>It's called the beautiful game for a reason. Nothing beats playing the game in its original state &mdash; outside, 11 versus 11, on the crisp, pristine, freshly cut grass of a pitch. However, the indoor sport of futsal is just as enjoyable as outdoor soccer and offers a wide range of benefits for both beginners and advanced players. Yours truly played futsal growing up, and it eventually became my main sport. At a place called Taquaral, I'd play pickup almost every weekend. I'd run a few laps around the park, then play games until blisters formed on my feet, ending the day with an &aacute;gua de coco. Anyways, enough about me &mdash; here are 11 ways futsal can improve your soccer skills and better prepare you for the next level.</p>
<h4>Goalkeeper Involvement</h4>
<p>Number one: keeper development. When you speak about development, futsal can help the keeper with reactions and the quantity of shots. In a single futsal game, the goalkeeper will face 20 to 30 shots and make numerous saves. This will help improve reaction, timing, and confidence.</p>
<h4>Goalkeeper Foot Skills</h4>
<p>Number two: keeper foot skills. The modern game requires keepers to be proficient with the ball &mdash; so much so that some managers, like Pep Guardiola, start their entire game strategy from the back. Futsal is a game that helps keepers become confident and precise with the ball at their feet. If you are a keeper, then futsal is the perfect foundational sport to improve in this area.</p>
<h4>Defenders in Futsal</h4>
<p>Number three: improving defenders. Long are the days when defenders were there to intimidate and kick the ball out. These days, defenders are just as skilled and technically sound as many midfielders. Some may even argue that the defenders of today's age might have been CDMs back 20 years ago. Futsal helps defenders with technical skills as well as marking players, since marking man-to-man and following your man is a major part of the futsal game.</p>
<h4>Quick Shots &amp; Finishing</h4>
<p>Number four: quick shots. Have you ever coached kids and noticed they do this big wind-up to prepare for shooting? They take several seconds to adjust their body and try to get the ball perfect before a shot. Well, futsal is a game where quick shots and reactions are necessary. Futsal will fix this issue.</p>
<h4>Faster Decision-Making</h4>
<p>Number five: decision-making. Futsal is a quick game. You don't have much time to sit and think. Your reaction and thought process will improve &mdash; and this will benefit you when you go to the outdoor game.</p>
<h4>Skill Development</h4>
<p>Number six: skill. Futsal is known for creating some of the best players in the world. Neymar, Messi, Ronaldinho, and R9 all came from a futsal base. But don't get this wrong &mdash; this isn't freestyle trickery. Futsal helps create extremely technical players with the ability to break down defenses and get the shot off. Futsal is not a freestyle trickery game, even though sometimes fancy tricks are used.</p>
<h4>Game Intensity</h4>
<p>Number seven: intensity. Futsal is a game of sprints and counterattack play. If you want to improve on intense play with good decision-making and counterattacks, then futsal will help.</p>
<h4>Composure Under Pressure</h4>
<p>Number eight: composure. I hear this a lot as a coach: "The player needs more composure with the ball. They get anxiety, make mistakes when they have the ball." A player gets composure when they get used to players near them, and they begin to be more confident. In futsal, you will have players on you, pushing you. This will help with composure. You will get used to the pressure from players forcing you to react. When you go to outdoor soccer, the intensity will be less, but your composure will be everlasting.</p>
<h4>Physicality in Futsal</h4>
<p>Number nine: physicality. You learn to shield and protect the ball &mdash; especially as a piv&ocirc;. The piv&ocirc; position, or top attacking player, will need to hold the ball and help bring the team up the court. All players will learn to shield and protect the ball. This will benefit them when moving to outdoor soccer.</p>
<h4>Movement, Triangles &amp; Spacing</h4>
<p>Number ten: movement and triangles. Futsal teaches the geometry of the game &mdash; movement, overloading sides, one-twos. There's nowhere to hide on a futsal court. The passing has to be perfect. You must move to receive the ball. If you make a mistake on the court, it will be blatantly obvious to you and everyone else. This helps players develop quickly.</p>
<h4>Modern Football &amp; Futsal</h4>
<p>Futsal is the perfect foundational sport for outdoor soccer. Modern football has actually transitioned to more similarities with a futsal game than it had 20 years ago. The modern outdoor game is physically demanding, with constant sprints giving less space and time for the players to think. They operate in tight quarters and must have better passing than in the past. They do lots of triangles and play from the back with keepers and defenders who are technically sound with the ball. The modern outdoor game has become a tactical possession sport that mimics futsal. Long gone are the days of booting the ball to the corner flag.</p>
<h4>Barcelona &amp; Tiki-Taka</h4>
<p>I'd even argue that futsal was the basis during the era of Barcelona's tiki-taka football. Iniesta, Xavi, Messi, and Dani Alves would move doing triangles, rotating, doing one-twos, and holding the ball, waiting for the perfect time to quickly attack and get the shot off.</p>
<p>What say you? Did I miss something? Let me know in the comments below.</p>
<p><em>Transcript lightly edited from YouTube captions for readability.</em></p>
</div></details>'''

P2_ART = '''<p class="rv">Why has the most successful national team in World Cup history looked so ordinary for a decade? In Part 1 of this series, Coach Roberto Avey &mdash; who grew up playing in Campinas, Brazil &mdash; breaks down clips from Brazilian journalists, pundits and ex-players to examine what's really happening inside the Sele&ccedil;&atilde;o and the CBF. It ends with a surprise: a very famous World Cup winner's campaign to fix it all.</p>
<div class="tkbox rv"><b>Key takeaways</b>
<ul>
<li><b>The decline is real but not unprecedented</b> &mdash; even the 2002 champions and the 1994 team struggled through qualifying (Rom&aacute;rio rescued the '94 side in the final qualifier).</li>
<li><b>The problems start at the top</b> &mdash; CBF power plays, back-room deals to hold power until 2034, ticket prices near half a month's minimum wage, empty stadiums.</li>
<li><b>The league works against the national team</b> &mdash; Brazil semi-ignores FIFA dates, shoving weekend fixtures into midweek and overloading players.</li>
<li><b>The Ancelotti handshake saga</b> &mdash; no contract, a year and a half of interim managers, then nothing.</li>
<li><b>The hope: R9</b> &mdash; Ronaldo's run for CBF president, and why a football man beats a career bureaucrat.</li>
</ul></div>
<h2 class="rv">A decade of decline</h2>
<p>The video opens with the question every Brazilian fan keeps asking: why has the Sele&ccedil;&atilde;o been so poor for roughly ten years? The first clips break down the final 2024 World Cup qualifier of the year against Uruguay &mdash; a flat 1&ndash;1 draw that was hard to watch, let alone cheer. The pundits add historical perspective: Brazil has had rough qualifying campaigns before, including the 2002 team that went on to win it all, and the 1994 side that needed two Rom&aacute;rio goals in the final qualifier just to reach the World Cup.</p>
<h2 class="rv">The federation problem</h2>
<p>From there, the analysis turns to the CBF. There's little direction, little hope, and no cohesion around the team &mdash; and at the top sits a president more focused on power plays than football. Ticket prices for national team games were raised to roughly R$600 &mdash; nearly half a month's minimum wage in Brazil &mdash; at year-end, and the stadium sat empty. As Roberto puts it: you're not watching a Ronaldinho or a Neymar out there, so why would fans pay that to watch mediocrity?</p>
<h2 class="rv">Why elite managers won't come</h2>
<p>Could a Guardiola or an Ancelotti fix the Sele&ccedil;&atilde;o? Any foreign manager will do due diligence &mdash; and they'll find a federation president cutting deals to stay in power until 2034, a domestic league that only pretends to respect FIFA dates (weekend games pushed to midweek, overloading players and sabotaging call-ups), and Copa Am&eacute;rica logistics so bad the team was stranded in the United States without flights home. The Ancelotti chapter says it all: a handshake agreement with no contract, a year and a half of interim managers &mdash; Ramon Menezes, Fernando Diniz &mdash; and then Ancelotti walked away.</p>
<h2 class="rv">The big reveal: R9 for CBF president</h2>
<p>The video closes with Ronaldo &mdash; R9, the original &mdash; announcing his campaign for CBF president. His mission: rescue Brazilian football, restore the confidence and respect Brazil once commanded worldwide, and elevate the leagues, players and managers globally. Roberto's case for him: playing experience at the highest level, real business experience, and worldly wisdom &mdash; versus a lifelong desk bureaucrat. As in the corporate world, when leaders who never worked the floor take over, the business suffers.</p>'''

P2_TR = '''<details class="rv"><summary>Full Video Transcript (condensed)</summary><div class="tr-body">
<p>So what's going on with the Brazilian national football team? Why have they been so poor the last several years &mdash; I would say the last 10 years, to be exact? I get this question a lot, from friends I play with, from kids I coach and train, and it's hard to understand why there's been such a drastic decline. Today I'm going to put together a few clips from Brazil &mdash; from journalists, pundits, as well as ex-players. We'll analyze them, and at the end I have a special surprise about an older World Cup-winning player, a very famous guy. This is going to be a series &mdash; we have a lot to talk about.</p>
<h4>The Uruguay game</h4>
<p>They're discussing the final game of 2024 against Uruguay in Brazil for World Cup qualifying. It was a 1&ndash;1 tie &mdash; a pretty slouchy game, hard to watch, hard to stand up and cheer. There have been other difficult campaigns: even the 2002 World Cup-winning team hardly qualified, and in 1994 Brazil had a lot of problems qualifying as well &mdash; Rom&aacute;rio had to come in and score two goals in the final qualifying game to advance them to the World Cup.</p>
<h4>The Sele&ccedil;&atilde;o's direction</h4>
<p>There's very little direction and very little hope. The cohesiveness is not there whatsoever. All of that is hurting the play &mdash; as well as the CBF president, who has this kind of inferiority complex where he tries to show he's the most powerful, the man in charge, doing all these political things. We have really good players, but they're not the lead player on their teams in Europe. There's Vini Jr &mdash; he shares that responsibility with other players at Real Madrid &mdash; but he doesn't play very well for the Sele&ccedil;&atilde;o. Maybe it's not fair to expect him to play like a Neymar, a Ronaldinho, or an R9 &mdash; but it is proper to have those expectations. If he wants the Ballon d'Or, he needs to play better for the Brazilian national team.</p>
<h4>The empty stadium</h4>
<p>The stadium was empty and it was extremely expensive &mdash; one of those power plays by the CBF president. He raised the prices and people don't go. Why would they? You're not watching a Ronaldinho, you're not watching a Neymar &mdash; you're watching a team playing mediocre football. Tickets went up to around R$600 at the end of the year &mdash; when the minimum wage is about R$1,400 in Brazil, that's nearly half a month's salary just to watch the Sele&ccedil;&atilde;o.</p>
<h4>Hiring a foreign manager</h4>
<p>They discuss bringing in a manager from overseas &mdash; a Pep Guardiola, a Carlo Ancelotti. But say we invite a foreign manager: they're going to do their research, talk to friends and past Brazilian players they've managed. They'll see the current CBF president doing power plays and back-room deals to stay in power for another 10 years, until 2034. Then they'll hear the Brazilian league doesn't respect the FIFA dates &mdash; during international windows, leagues in England, Spain, Italy and the USA stop for about 10 days; in Brazil they semi-stop, pushing weekend games to midweek. If you're the national team coach and want to call up a player from the Brazilian league, it becomes very difficult &mdash; the player is overloaded. Then, logistically: during Copa Am&eacute;rica, Brazil didn't have flights home and had to stay an extra day in the United States because someone mismanaged the travel. Five-time world champions &mdash; and it's that unorganized. It's hard to bring in a Guardiola or an Ancelotti and expect them to want to join complete disorder.</p>
<h4>The Ancelotti saga</h4>
<p>The CBF president did a handshake deal with Carlo Ancelotti, the Real Madrid manager, to take over the Sele&ccedil;&atilde;o. For a year and a half we had interim managers &mdash; Ramon Menezes, Fernando Diniz &mdash; and it was poorly managed. Nothing was written on paper, there were no contracts. After a year and some months, Ancelotti said: I don't want to be part of this.</p>
<h4>The reveal &mdash; R9</h4>
<p>Who's going to be the next CBF president? R9. Ronaldo &mdash; the original, the real one. The gods of football blessed Ronaldo with speed, ability, agility, force, and wisdom in the sport. Why does he want to become president of the Brazilian Federation? He said it clearly: he wants to rescue football in Brazil, bring back the confidence and respect Brazil had throughout the world, and elevate the leagues, the players and the managers globally. I feel he has the capacity to do it. He has the playing experience, he's been in business for a while, he's not a lifelong bureaucrat or politician. Being a leader takes sternness, confidence, and most of all critical thinking. We've all been in situations with that sort of character &mdash; a lifelong person behind the desk who never applied anything, suddenly becomes a leader, and two or three years later there are layoffs everywhere. It's time to get someone who actually worked in the industry from the ground up.</p>
<p>I'm happy R9 is doing this &mdash; I think he has the capacity. I'd love to hear what you have to say: put comments below in English, Portuguese, Spanish, Italian &mdash; whatever you feel. Like and subscribe: I'm going to do several more of these videos about the CBF, the Sele&ccedil;&atilde;o, Vini Jr and other players. Talk to you soon &mdash; t&aacute; bom?</p>
<p><em>Transcript lightly edited from YouTube captions for readability; Brazilian names and terms corrected.</em></p>
</div></details>'''

P3_ART = '''<p class="rv">"We are being the worst team maybe in the history of Manchester United." When Ruben Amorim said that in a live press conference, it made every headline in world football. Coach Roberto Avey breaks down the clips and asks the bigger question: is that how a leader takes over a struggling team? The lessons apply far beyond football &mdash; to business, coaching, and any new leadership role.</p>
<div class="tkbox rv"><b>Leadership lessons from the breakdown</b>
<ul>
<li><b>Never badmouth your team in public.</b> Say what you need behind closed doors &mdash; never in front of the world.</li>
<li><b>The new leader owns part of the problem.</b> If the team performs worse after you arrive, you're a big percentage of the issue.</li>
<li><b>Adapt your system to your people.</b> You can't run "your style" at 100% with players who don't fit it &mdash; run it at 50% until you have your people.</li>
<li><b>Don't be stubborn when you can see the iceberg.</b> Roll with the punches, move roles around, pivot.</li>
<li><b>Leadership needs training.</b> Football is a business &mdash; press and people skills don't come automatically from 20 years of kicking a ball.</li>
</ul></div>
<h2 class="rv">"Don't hold back, buddy"</h2>
<p>The breakdown opens with the quote itself. Roberto's reaction: whoa &mdash; is that how you feel about your team? Imagine a new leader in a company walking in and announcing "my team sucks." You will get nothing out of your players &mdash; or your employees &mdash; after that. A new coach losing more games than the last coach is a huge part of the problem himself: the players don't want you yet, and you can't impose your system at 100% before your own players arrive.</p>
<h2 class="rv">The headlines write themselves</h2>
<p>"You want headlines? Here are your headlines: MY TEAM SUCKS." Roberto asks whether Amorim has had any press training at all &mdash; because football is a business, just like the one you walk into every morning. Reaching a leadership position requires leadership skills, no matter how long you've been on the pitch. And if you're going to be cheeky off the cuff, you'd better back it up with results.</p>
<h2 class="rv">What Amorim got right</h2>
<p>To be fair, the clips also show Amorim owning the moment: "Everybody here is underperforming... it's unacceptable to lose so many games for any club in the Premier League &mdash; imagine Manchester United... we have to continue, there is no other way. We need to suffer." He admits he knew installing a completely new idea mid-season would be hard. The honesty is real &mdash; the delivery is the problem.</p>
<h2 class="rv">If you lead a new team, listen</h2>
<p>Roberto closes with the playbook for anyone taking over a struggling team: never badmouth your people, publicly or otherwise. Get the most out of the team you have. Change responsibilities and roles; move people around. Don't be hard-headed, don't be stubborn &mdash; roll with the punches and pivot. And a wink to finish: "Amorim, we're thankful you're here &mdash; you're definitely better than the last guy. Then again, anybody could have been better than the last guy."</p>'''

P3_TR = '''<details class="rv"><summary>Full Video Transcript</summary><div class="tr-body">
<p><b>Amorim (clip):</b> "So, um, we are being the worst team maybe in the history of Manchester United."</p>
<p><b>Roberto:</b> Whoa, whoa, whoa buddy &mdash; don't hold back! Is that how you feel about your team, about your players? Is that what we're getting when a new coach &mdash; that is losing more than the last coach &mdash; comes in? You're 60% of the problem. They were playing worse, you knew what you were coming into, you have players that don't want you. You can't play Amorim-style football 100% &mdash; you've got to do Amorim-style football 50% until you get your new players in.</p>
<p><b>Amorim (clip):</b> "That's it. I'm not going to change, no matter what."</p>
<p><b>Roberto:</b> Is this the moment to be hard-headed? You see the iceberg ahead of you and you're going to drive right into it, Mr. Titanic? What's going on?</p>
<p><b>Amorim (clip):</b> "I know we can succeed, but we need to survive this moment, because I'm not naive and I know that we need to survive now... we are being the worst team maybe in history of Manchester United."</p>
<p><b>Roberto:</b> The worst team in the history of Manchester United &mdash; whoa, let us know how you really feel! Is that how a leader comes into a new gig? Can you imagine in corporate, or in your own business, somebody comes in: "my team sucks"? Amorim, you're a big part of the issue, man. You're not going to get anything out of your players by saying they suck. You can say whatever you want to them behind closed doors, in the locker room, on the training pitch &mdash; but in front of everyone else, you can't say that type of stuff. I know you want headlines... well, here you go, here are your headlines: MY TEAM SUCKS. Has this guy had any press training? This is insane. Listen &mdash; football is a business, just like corporate. You have to have had some type of training when you get to a leadership position. I don't care if you've been kicking a ball around for the last 20 years &mdash; you have to have those leadership skills. You can be a little bit cheeky, off the cuff &mdash; that's fine. But if you're going to be off the cuff and cheeky, you'd better demonstrate it on the pitch.</p>
<p><b>Amorim (clip):</b> "Everybody here is underperforming. No matter the circumstances, we are underperforming and we have to accept that. It's unacceptable to lose so many games for any club in the Premier League &mdash; imagine Manchester United. So it's a really hard moment, but we have to continue. There is no other way. We need to suffer and continue. I knew it was going to be hard to put a completely new idea in this moment, but when you lose games you don't have that luck. That's why I'm telling you we are going to suffer &mdash; because I will continue to do the same."</p>
<p><b>Roberto:</b> If you're a leader, this is a great example of what NOT to do when you're coming into a difficult new position. Don't badmouth your team &mdash; ever. Try to get the most out of the players, out of your team members. Change responsibilities and roles, move people around. Don't be hard-headed. Do not be stubborn. Roll with the punches &mdash; pivot, change. Amorim, we're thankful you're here at Manchester United. You're definitely better than the last guy... well, I think anybody could have been better than the last guy.</p>
<p><em>Transcript lightly edited from YouTube captions for readability.</em></p>
</div></details>'''

data = {'posts': [
 {'id': 1307, 'slug': 'why-futsal-creates-better-soccer-players', 'vid': 'I2FljcfwqT4',
  'kicker': 'Video Blog &middot; Player Development',
  'h1a': 'Futsal Builds', 'h1sky': 'Complete Players.',
  'yt_title': 'Why Futsal Creates Better Outdoor Soccer Players (11 Reasons)',
  'yt_title_plain': 'Why Futsal Creates Better Outdoor Soccer Players (11 Reasons)',
  'wp_title': 'Futsal Builds Complete Players',
  'desc': "Coach Roberto Avey breaks down 11 ways futsal creates better outdoor soccer players — keeper reactions, quick shots, composure, movement and more.",
  'up': '2026-01-07', 'meta': '6 min watch &middot; Coach Roberto Avey &middot; <a href="https://www.youtube.com/watch?v=I2FljcfwqT4" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>',
  'card_desc': "The 11 ways futsal develops keepers, defenders and attackers faster than the outdoor game — and why modern football now mimics the futsal court.",
  'article': P1_ART, 'transcript': P1_TR},
 {'id': 1308, 'slug': 'whats-wrong-with-brazil-national-team-part-1', 'vid': 'VdEe1E8CLj8',
  'kicker': 'Video Blog &middot; Brazilian Football',
  'h1a': 'The Fall of the', 'h1sky': 'Sele&ccedil;&atilde;o.',
  'yt_title': "What's Wrong With Brazil's National Soccer Team &mdash; Part 1",
  'yt_title_plain': "What's Wrong With Brazil's National Soccer Team - Part 1",
  'wp_title': 'The Fall of the Seleção — Part 1',
  'desc': "Coach Roberto Avey analyzes clips from Brazilian journalists and ex-players on the CBF, empty stadiums, the Ancelotti saga, and R9's run for CBF president.",
  'up': '2024-12-21', 'meta': '20 min watch &middot; Coach Roberto Avey &middot; <a href="https://www.youtube.com/watch?v=VdEe1E8CLj8" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>',
  'card_desc': "A decade of decline, CBF power plays, the Ancelotti handshake saga — and why R9's run for president might be the rescue Brazilian football needs.",
  'article': P2_ART, 'transcript': P2_TR},
 {'id': 1309, 'slug': 'amorim-press-conference-leadership-lessons', 'vid': 'Nlx8qWqa1zY',
  'kicker': 'Video Blog &middot; Leadership',
  'h1a': 'How Not to Lead', 'h1sky': 'a New Team.',
  'yt_title': 'Amorim Press Conference &mdash; How To Be A Leader in Tough Situations (Manchester United)',
  'yt_title_plain': 'Amorim Press Conference - How To Be A Leader in Tough Situations Manchester United',
  'wp_title': 'How Not to Lead a New Team — Amorim Edition',
  'desc': "Ruben Amorim called Manchester United 'maybe the worst team in history.' What his press conference teaches about leading a struggling team — in football and business.",
  'up': '2025-01-28', 'meta': '5 min watch &middot; Coach Roberto Avey &middot; <a href="https://www.youtube.com/watch?v=Nlx8qWqa1zY" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>',
  'card_desc': "Amorim called his own squad the worst team in United's history. The leadership playbook of what to do — and what never to do — with a struggling team.",
  'article': P3_ART, 'transcript': P3_TR},
]}
json.dump(data, io.open('videoposts_bodies.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('bodies written:', [p['slug'] for p in data['posts']])
