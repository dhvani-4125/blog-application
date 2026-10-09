"""Editorial content for THE WITHIN (a fictional portfolio concept).

All articles are original writing. Nothing here is medical advice.
Body text: paragraphs separated by a blank line; lines starting with "## " are subheadings.
"""

CATEGORIES = [
    ("Mind", "mind", "Emotional wellbeing, relationships, self-awareness and reflection.", "Notice what is going on inside.", 1),
    ("Body", "body", "Movement, mobility, strength, recovery and rest.", "Move in a way that suits you today.", 2),
    ("Nourish", "nourish", "Nutrition, mindful eating and our relationship with food.", "Food as more than fuel.", 3),
    ("Ritual", "ritual", "Mindfulness, meditation, journaling, spirituality and everyday rituals.", "Small, repeatable things that matter.", 4),
    ("Relationships", "relationships", "Conversation, boundaries, closeness and being understood.", "How we are with each other.", 5),
    ("Rest", "rest", "Sleep, slowness, doing less and learning to stop.", "Permission to stop.", 6),
]

EDITORS = [
    ("maren.ellison", "Maren", "Ellison"),
    ("theo.brandt", "Theo", "Brandt"),
    ("ines.calloway", "Ines", "Calloway"),
    ("jonah.whitlock", "Jonah", "Whitlock"),
]

# (title, category slug, editor index, days ago, featured, excerpt, image alt, body)
ARTICLES = [
(
"Why Rest Doesn't Always Feel Restful", "mind", 0, 6, True,
"You finally have a free afternoon and somehow it leaves you more unsettled than before. That is common, and it is worth understanding.",
"A folded blanket and an open window in soft afternoon light",
"""The plan was simple. Nothing on the calendar, a cup of tea, a sofa. By four o'clock you are checking your phone for the ninth time and feeling oddly worse than you did on Wednesday, when you were run off your feet.

Plenty of people recognise this. Busyness gives the mind a job. When the job disappears, whatever it was keeping at a distance gets a chance to speak: a conversation you have not had, a decision you keep postponing, a low hum of tiredness you had learned to talk over.

That does not mean something is wrong with you, or with rest. It usually means your body and your attention are out of step. Your body has stopped, and your mind is still running at the old speed.

## Rest is a skill as well as a state

Many of us were never taught to rest, only to earn it. If a break has always come after a task is finished, a break with no task in front of it can feel like trespassing. It helps to start smaller than an afternoon. Ten minutes by a window. A slow cup of something warm without a screen next to it.

Notice what turns up, and let it be unremarkable. You are not trying to solve it. You are letting it be there while you sit somewhere comfortable.

## Different kinds of rest

Lying on a sofa is one kind. A walk with no destination is another. So is cooking something simple, or sitting in a room with a friend and not talking. If one kind leaves you restless, try another before deciding that you are bad at it.

If the restlessness is heavy, or has been going on for a long time, it is worth talking to someone you trust, or a qualified professional. Until then, you can treat it as information rather than a failing, and try a gentler version of rest tomorrow."""
),
(
"When Rest Starts Feeling Uncomfortable", "mind", 2, 20, False,
"Stillness can bring up things that a busy week keeps quiet. A few thoughts on staying with it, and on when to ask for company.",
"An empty chair beside a window with the curtain moving slightly",
"""There is a particular kind of discomfort that arrives the moment you sit down. It is not pain, exactly. It is more like an itch to get up and be useful.

Most of us have built a life that rewards motion. Replying quickly, being available, having something to report. Against that background, stillness can feel like falling behind. The discomfort is often the sound of an old habit objecting.

Sometimes it is something more specific. A quiet evening makes room for a worry that has been waiting. You notice you are sad about something, or angry, and had not had time to know it.

You do not have to sit in that for long, or alone. A reasonable approach is to rest in short pieces, and to pick things that keep a little company with your attention: a bath, a slow walk, a book you already love. Gentle structure can make stillness easier to approach.

If the same feelings keep returning, writing them down can take some of their weight. Saying them out loud to a friend, or to a therapist, can take more. There is no prize for managing it by yourself.

Over time, many people find the itch softens. Not because they got better at doing nothing, but because the quiet stopped being a threat and became just another room in the house."""
),
(
"The Difference Between Being Alone and Feeling Lonely", "mind", 1, 34, False,
"One is a circumstance and the other is a feeling. They overlap less often than we assume.",
"A single cup on a table by a rain-streaked window",
"""You can spend a whole Sunday by yourself and feel entirely well. You can also stand in a crowded room and feel like you are watching through glass.

Being alone is a fact about who is in the room. Loneliness is a feeling about the gap between the connection you have and the connection you want. They sometimes travel together, but they are not the same thing, and mixing them up can lead us to the wrong remedy.

If you assume loneliness means too much solitude, you might fill your calendar and feel no better. If the real gap is feeling understood, a full week of small talk will not close it. One honest conversation might.

## Telling them apart

It can help to ask a plain question: what am I missing right now? Sometimes the answer is company. Sometimes it is being known by someone, or having a person to tell about the small thing that happened this morning. Sometimes it is a sense of belonging to something larger than your own routine.

Solitude, by contrast, can be a pleasure when you choose it. Many people find they think more clearly alone, or that their creativity needs it.

If loneliness has become heavy or constant, it deserves to be taken seriously and not just endured. Start with one small step towards a person: a message, a coffee, a class where the same faces turn up each week. Connection tends to build from repetition more than from big gestures."""
),
(
"When a Good Day Still Feels Heavy", "mind", 3, 48, False,
"Nothing went wrong, and still something sits on your chest. On heaviness without an obvious reason.",
"Late sun across a quiet kitchen table with an open notebook",
"""The day went fine. Work was fine, dinner was fine, someone was kind to you. And yet, by evening, there is a weight you cannot point at.

We tend to look for a cause, because a cause suggests a fix. When there isn't one, it is easy to turn on ourselves: I have nothing to be sad about, so why am I like this?

Feelings do not always arrive with a reason attached. Tiredness that has built over weeks, a hard anniversary you did not register, a long stretch of pushing on, changes in the season. Sometimes the body keeps a ledger the mind has not read yet.

A few things that people find useful, offered gently. Describe the feeling in plain words instead of arguing with it. "Heavy" or "flat" is enough. Lower the demands of the evening, even slightly. Eat something. Go outside for a few minutes if you can.

Try not to add a second layer of judgement on top of the first. Feeling heavy on a good day is not ungrateful. It is simply what is true at the moment.

If the heaviness stays for weeks, affects your sleep or appetite, or makes ordinary tasks hard, it is a good reason to speak to a doctor or a mental health professional. You do not need a dramatic reason to ask for support."""
),
(
"What Does Feeling Like Yourself Actually Mean?", "mind", 2, 62, False,
"We say we want to feel like ourselves again. It is worth asking which self we mean.",
"A mirror leaning against a wall, reflecting a plain window",
"""People often say they want to feel like themselves again. It is a lovely phrase, and a slippery one. Which self, and from when?

Usually, the phrase points to a handful of specific things. You laughed more easily. You had energy for the people you like. You made decisions without a long argument in your head. When we unpack it, we tend to find a list of experiences instead of a fixed identity.

That is useful, because experiences can be approached. If you remember that you used to feel most like yourself after a long walk on a Saturday, that is something you can try to bring back. It is more practical than trying to find a lost version of you.

It is also worth allowing that the person you were two or five years ago may not be the right target. Circumstances change us. Loss, work, parenthood, age. Part of feeling like yourself can be getting to know who you are now, and checking in on what that person needs.

A simple exercise: write down three moments from the past year when you felt at home in yourself. Look for what they share. The company, the setting, the pace. Then ask what small piece of that you could invite into next week.

You do not have to become someone else. You may only need to stop living entirely at the pace of everyone else's expectations."""
),
(
"Learning to Sit With an Uncertain Answer", "mind", 0, 90, False,
"Not knowing is uncomfortable, and we hurry to end it. Some thoughts on leaving a question open for a while.",
"A path disappearing into soft morning mist between trees",
"""Most of us dislike open questions. Should I change jobs, end this, move, say yes. We want the answer so that the discomfort can stop.

The urge to decide quickly is often about relief and not about readiness. A bad answer can feel better than no answer, simply because it ends the waiting. That is worth noticing before we sign anything.

Sitting with uncertainty does not mean doing nothing. It can mean gathering what you can, talking to people who know you, and then allowing time for the rest to settle. Some decisions get clearer when we sleep on them. Others don't, and in those cases you may need to choose without certainty and accept that.

One thing that helps is separating what you do know from what you are guessing. Write both lists. The known list is often longer than expected, and the guessing list shows where you could ask a question or run a small experiment.

It also helps to notice how you talk to yourself while you wait. If every day of not knowing feels like a failure, it will be a hard wait. If you can treat it as part of the process, the same days feel lighter.

Some answers need time to arrive. Giving them that time is not avoidance. It can be one of the more careful things we do."""
),
(
"A Beginner's Guide to Moving More Gently", "body", 1, 12, False,
"You do not need a new routine or new shoes. You need a small, kind place to start.",
"Bare feet on a wooden floor beside a rolled yoga mat",
"""If you have not moved much lately, the idea of starting can feel like a lot. The internet offers programmes with names like challenge and transformation. You can set all of that down.

Moving gently means choosing movement that you could imagine doing again tomorrow. It should leave you feeling the same or a little better, not flattened.

## Start with what already exists

Stretch when you get up. Walk to the end of the road and back. Take the stairs when there are only two flights. These are not warm-ups for real exercise. They are real, and they add up.

## Choose by feel, not by rule

Some people like rhythm, such as walking or cycling. Others prefer slow strength work or a mobility class. You are allowed to try several and drop the ones that make you dread them. Enjoyment is one of the best predictors of whether you will keep going.

## Keep it small enough to repeat

Ten minutes is plenty. If it turns into twenty, good. If it stays at ten, also good. Missing a day is not a reset. You simply go again.

A note on bodies: if you have an injury, a health condition, or you are returning after illness, check with a doctor or physiotherapist about what is suitable. Gentle does not mean the same for everyone.

What you are building is a relationship with your body in which movement is something you do with it, not to it."""
),
(
"Why Strength Can Be a Form of Self-Care", "body", 3, 27, False,
"Getting stronger is not only about appearance. It can be about carrying the shopping, climbing stairs and trusting your body.",
"Hands gripping a plain iron kettlebell on a wooden floor",
"""Strength training has a reputation problem. For many people it still conjures up mirrors and numbers. That image misses a lot of what it can offer.

Think about the ordinary things a body does. Lift a bag, get up from the floor, carry a child, push a heavy door, climb a hill without stopping to recover. Being stronger makes those things easier, and often makes them feel less like an effort.

There is also the matter of trust. When you practise lifting something and find, a few weeks later, that it feels lighter, you collect small evidence that you can change. That quiet sense of capability tends to leak into other parts of life.

## Starting without drama

You do not need a gym membership. Bodyweight movements like sit-to-stands, wall push-ups and step-ups are a perfectly respectable beginning. If you want to add weight later, a pair of dumbbells or a resistance band is enough.

Go slowly and focus on how the movement feels. Rest between sets. Stop if something hurts in a sharp or worrying way, and speak to a professional if it keeps happening.

## Making it yours

Strength can be a twenty-minute session twice a week. It does not have to be about getting smaller or bigger or fitting any shape. It can simply be about being a person who can do what they need to do, with a little more ease."""
),
(
"The Case for Taking a Slower Walk", "body", 1, 41, False,
"A walk without a target pace has its own benefits. Mostly, it lets you notice where you are.",
"A narrow lane with tall hedges and dappled light",
"""Somewhere along the way, walking turned into a metric. Steps, pace, calories. Those numbers have their uses, but they can turn a pleasant habit into another thing to get right.

A slower walk asks for nothing. You leave without a route and without headphones, if you like. You allow yourself to stop when something catches your eye: a wall with moss on it, a neighbour's overgrown garden, the sound of a school playground at lunchtime.

Walking slowly does something interesting to attention. At speed, you pass through a place. At a slower pace, you start to be in it. Many people find their thinking loosens too, perhaps because the body is occupied with a simple rhythm and the mind can wander without being chased.

Practicalities are minimal. Choose a time of day when you are not rushing to be elsewhere. Wear shoes you do not have to think about. If you want a rule, make it this one: no checking the time for the first twenty minutes.

If walking is difficult for you for any reason, the same spirit can be applied to sitting outside, wheeling slowly through a park, or spending time at an open window. The point is not the mileage. It is giving yourself a stretch of the day where you are not trying to arrive."""
),
(
"What Your Body Might Need on a Tired Day", "body", 3, 55, False,
"Tired is not one thing. Some questions to ask before you decide whether to push on or stop.",
"A rumpled linen bed seen from above in morning light",
"""Tiredness arrives in different forms, and treating them all the same can make things worse.

There is the tiredness of a bad night. There is the heavy, muddy kind that follows days of stress. There is the restless sort, when you are exhausted and wired in equal measure. And there is the tiredness of sitting still all day, which can ease with a bit of movement.

Before deciding what to do, ask a few simple questions. Have I eaten and had water recently? Have I been outside? How did I sleep? Is this a physical tiredness, or more of a flat, mental one?

Often a little gentle movement helps when you have been inert. A short walk or a few minutes of stretching can lift a slump. If the tiredness feels deeper, as though you have nothing in reserve, then rest is a perfectly reasonable response. Cancel the extra thing. Go to bed early. Make something simple for dinner.

It is worth keeping a loose record over a few weeks, just a line or two each evening. Patterns tend to show: perhaps you are always flat after a certain meeting, or on the days you skip lunch.

If tiredness is persistent and unexplained, or comes with other symptoms, please speak to a doctor. Ongoing fatigue is something to have looked at, not something to push through."""
),
(
"Movement Without the Pressure to Perform", "body", 0, 76, False,
"Not every session has to be productive. Some of the best ones are just a body moving because it can.",
"A person's silhouette stretching near a sunlit window",
"""There is a kind of movement that exists only to be measured. Faster than last week, heavier, longer, tidier. It has its place. But when it becomes the only kind, exercise starts to feel like another performance review.

Try, once in a while, moving with no outcome. Put on a record and sway around the kitchen. Roll your shoulders on the floor. Lie on your back and let your knees fall from side to side. Stretch like a cat does after sleeping, with no idea what comes next.

This kind of movement asks you to listen, not to push. Where does the body want to go? What feels stiff, and what feels easy? You might find you like something you would never have chosen from a class list.

For people who feel self-conscious about exercising, this can be an easier way in. Nobody is watching and nothing is being graded.

It also helps to think about what you tell yourself while moving. If the voice in your head is relentlessly critical, the session is going to feel like work. If you can soften it, even slightly, movement becomes something closer to company.

A week of two or three informal sessions is enough to notice a difference in how you relate to your body, and perhaps to how you approach the more structured sessions too."""
),
(
"What Does Eating Well Actually Mean?", "nourish", 2, 9, False,
"The phrase is used constantly and defined rarely. Perhaps it deserves a more personal answer.",
"A wooden table set with bread, olive oil and seasonal vegetables",
"""Ask ten people what eating well means and you will get ten answers. Lots of vegetables. No sugar. Three meals. Never after eight. Whatever the latest book says.

Underneath those rules, there is usually a quieter wish: to feel nourished, to enjoy food, and to not spend so much of the day thinking about it.

For some people, eating well is mostly practical. Regular meals, a variety of foods, enough to feel satisfied. For others it includes the social side, such as feeding people, sharing a table, or cooking something that reminds them of home. And for others, it involves working with a health professional on specific needs, which is a different and valuable thing.

A helpful definition might be this: eating in a way that supports your body, suits your life, and doesn't make you miserable. That leaves room for a Tuesday salad and a Friday chip shop supper.

If you want a place to begin, try noticing instead of fixing. How do you feel after different meals? What do you enjoy? When do you eat without noticing? None of this requires a plan, only some curiosity.

If food has become a source of anxiety, or you find yourself following rules that frighten you when you break them, a dietitian or therapist who works with eating can help. That is not a failure of willpower. It is a good reason to ask for support."""
),
(
"The Ritual of Cooking for Yourself", "nourish", 1, 23, False,
"A meal for one is easy to treat as an afterthought. It can be one of the better parts of the day.",
"A small pan on a stove with sliced onions and a wooden spoon",
"""Cooking for other people comes with a built-in reason. Cooking for yourself often doesn't, so dinner becomes toast over the sink or whatever is quickest.

There is nothing shameful about toast. But if you notice a flatness around meals when you are alone, it might be worth treating one of them as a small occasion.

You do not need a recipe with twelve ingredients. Start with something you like and can make without stress: eggs done the way you enjoy them, a pot of soup, pasta with good olive oil and plenty of black pepper. Lay the table properly, even if it is only for you. Use the plate you like.

The act of cooking has its own pleasures. The sound of onions softening. The smell that fills the kitchen. The way a simple process asks for just enough attention to quiet your thinking.

Some find it helps to choose one evening a week for this and treat the rest as flexible. Others cook a larger batch on Sunday and eat well all week without thinking. Both are fine.

What matters is the message you send yourself. When you take a few minutes to prepare something and sit down with it, you are saying that you are worth the effort. That is a modest, repeatable form of care."""
),
(
"Learning to Eat Without Rules", "nourish", 2, 44, False,
"Food rules promise calm and often deliver the opposite. A look at what it might be like to loosen them.",
"A shared bowl of fruit on a linen cloth",
"""Food rules are seductive. They offer certainty. If I follow this, I will feel in control. And for a while, that can be true.

The trouble tends to arrive later. Rules need constant management, and every exception becomes a small crisis. Meals become tests that you pass or fail. Food, which is supposed to be a basic pleasure, takes on a moral charge.

Eating without rules does not mean eating without thought. It means swapping external instructions for internal information. Am I hungry? What sounds good? Am I full? Did I enjoy that? These questions are harder to answer at first, especially if you have ignored them for years, but they tend to get clearer with practice.

You can begin with one small experiment. Choose a food that carries a rule, say a certain biscuit, and have it on a calm afternoon, sitting down, paying attention. Notice what it tastes like. Notice whether you wanted more, and what happened when you did or didn't have it.

Be patient with yourself. Loosening rules can bring up anxiety, and it may need to happen gradually.

If you have a history of disordered eating, or if the idea of dropping rules feels frightening, please work with a professional who understands this area. Support makes the process safer and kinder."""
),
(
"Why Food Can Be About More Than Nutrition", "nourish", 3, 71, False,
"A bowl of soup can be comfort, memory and care at once. That is part of what food is for.",
"A pot of soup being ladled into a ceramic bowl",
"""When we talk about food in wellness circles, the conversation often narrows to nutrients. Protein, fibre, vitamins. They matter. But they are not the whole story.

Think of the food that connects you to someone. A grandmother's stew, a birthday cake, the tea someone made when you were ill. Those meals carry memory and affection. They are part of how we mark time and show love.

Food is also how we gather. Sharing a table makes room for conversation that doesn't happen elsewhere. It is how many cultures celebrate, grieve and welcome new people.

None of this contradicts caring about nutrition. It just widens the frame. A meal can be good for your body and good for your spirit, and sometimes one of those is the main point of the evening.

If you have been treating food only as fuel or only as something to manage, you might try noticing the other things it does for you. Who do you eat with? Which meals do you look forward to? What do you cook when you want to feel looked after?

These questions help restore a sense of proportion. They also make it easier to make choices that are about enjoyment and not about fear. Food was never meant to be a daily exam."""
),
(
"Five Minutes to Come Back to Yourself", "ritual", 0, 15, False,
"A short, repeatable pause for the middle of a loud day. No equipment, no special skills.",
"A cup of tea steaming on a windowsill",
"""Some days are so crowded that you reach the evening without having noticed any of them. A short pause can help you catch up with yourself.

Here is one way to do it. It takes five minutes, and you can do it at a desk, in a car park or at the kitchen counter.

First, stop. Put down whatever is in your hands. Sit or stand somewhere you can be still for a moment.

Second, notice your feet. Feel them on the floor. Let your weight settle through them. This is a quiet way to arrive in your body.

Third, take a few slower breaths, not forced or deep, just a little slower than your usual. If your mind wanders, which it will, bring it back without scolding.

Fourth, ask a simple question: what do I need right now? You might hear nothing, or you might hear water, a walk, or a phone call. Whatever comes is useful.

Finally, take a last breath and go back to your day, a little more present than before.

Rituals like this work because they are small. They fit around the edges of real life. Over time, the pause itself starts to feel like a place you can return to, which is a good thing to carry with you."""
),
(
"What Makes a Ritual Feel Meaningful?", "ritual", 2, 38, False,
"The same action can be a chore or a ritual. The difference tends to be attention and intention.",
"A candle, a notebook and a pen arranged on a small table",
"""Making coffee can be a chore or a ritual. The difference is not the coffee. It is how you do it.

A ritual usually has a few features. It is repeated, so it has a shape you can recognise. It has a clear beginning and end. And it is done with some attention, which separates it from habit that runs on autopilot.

Meaning comes from what the ritual connects you to. Perhaps it marks the shift from work to home. Perhaps it honours someone, or a season, or a value you care about. Lighting a candle at the end of the day can say: the working part is over.

It does not need to be elaborate or spiritual, although it can be. A few quiet minutes with a notebook can be as meaningful as an elaborate ceremony, if it matters to you.

If you want to build one, start by asking what you would like to mark or protect. Then choose a simple action that fits, and tie it to something that already happens in your day. After breakfast, before bed, when you get home.

Give it time. A new ritual often feels awkward for the first couple of weeks. If it still feels like an obligation after that, change it. A ritual should serve you, and it is allowed to evolve."""
),
(
"A Different Way to Think About Meditation", "ritual", 1, 66, False,
"Meditation is often described as emptying the mind. Many practitioners describe it quite differently.",
"A simple cushion by a wall in an otherwise empty room",
"""A common idea about meditation is that you are meant to stop thinking. People try it, find that their mind is full of shopping lists, and decide they are no good at it.

Many teachers describe the practice differently. The aim is not to stop thoughts. It is to notice that you are thinking, and to return, again and again, to something simple like the breath. The returning is the practice. A mind that wanders off twenty times and comes back twenty times has done twenty repetitions.

Seen that way, there is no such thing as a bad session. A restless one is just a different one.

If sitting still is difficult, there are other ways in. Some people prefer walking meditation, paying attention to the feel of each step. Others like to focus on sounds, or on the sensations of washing up. Guided recordings can help at first.

Short sessions are fine. Five minutes a day is more sustainable than thirty minutes once a month.

A caution worth stating: for some people, particularly those dealing with trauma or severe anxiety, sitting quietly with their thoughts can be difficult. If that is you, it is reasonable to talk to a therapist or an experienced teacher before continuing. Meditation is one tool among many, and it does not have to suit everyone."""
),
(
"Small Rituals for Busy Days", "ritual", 3, 82, False,
"When life is full, big routines collapse. Tiny ones tend to survive.",
"Keys in a ceramic dish by a front door",
"""When the week is chaotic, the thirty-minute morning routine is the first thing to go. Then comes the guilt about having dropped it.

A more forgiving approach is to build rituals so small that they survive a bad week. Think in seconds and minutes, and tie them to things you already do.

Here are some that people find workable. A full glass of water before the first coffee. Three slow breaths before opening your laptop. Putting your keys in the same dish and pausing for a moment as you do it. Writing one line in a notebook before bed. Looking out of a window while the kettle boils.

None of these would impress anyone, which is rather the point. They can happen on the train, in a lift or in a bathroom. They give you a handful of anchor points through the day, each one a chance to arrive back in yourself.

If you want to add something, add one at a time and give it a couple of weeks before judging it.

On the days when even these slip, you haven't failed. You have had a busy day. You pick them up again on the next one.

Over a season, small rituals can quietly change the feel of an ordinary week. Not dramatically, but in a way you notice when they are missing."""
),
(
"The Conversations We Keep Avoiding", "relationships", 0, 18, False,
"There is usually one. It gets heavier the longer it waits, and often smaller once it happens.",
"Two mugs on a table between two empty chairs",
"""Most of us have one. A conversation we rehearse in the shower and never begin. About money, or a habit that wears us down, or a thing that was said years ago.

We avoid these talks for understandable reasons. We do not want to hurt anyone. We do not want a row. We tell ourselves it is not worth it. In the short term, avoiding feels like kindness.

The cost shows up later. Resentment builds quietly. The relationship gets a little more careful and a little less close.

## Making it easier to start

Choose a calm time, not the middle of an argument. Say plainly what you want: "I'd like to talk about something that's been on my mind. Is now okay?" Speak about your own experience, which is harder to argue with than a list of their faults.

Keep it short at the beginning. You do not have to solve everything in one sitting. Sometimes the most important part is simply that it has been named.

## Listening matters as much as speaking

The other person may see things differently, and may be surprised. Give them room to respond. You might find that what you feared was far less dramatic than it seemed.

If the topic is very difficult, or if you feel unsafe, it can help to involve a counsellor or mediator. There is no weakness in asking for help to say something hard."""
),
(
"Learning to Ask for What You Need", "relationships", 2, 33, False,
"Many of us expect others to guess. Asking out loud is more direct, and usually more fair.",
"A hand resting on a table beside another open hand",
"""Plenty of us were raised to be low-maintenance. To not make a fuss, to be easy. The side effect is that we struggle to say what we need, and then feel quietly let down when nobody notices.

Hinting feels safer than asking. If you hint and nothing happens, you have not technically been refused. But the people around you are not mind readers, however well they know you, and hints are easy to miss.

Asking directly is a skill that can be learned. A good request is specific, kind and has room for a no. "Could you take the children on Saturday morning so I can have a couple of hours?" is clearer than "I never get any time to myself."

It helps to know what you need before you speak. Sit with the question for a few minutes. Is it practical help, a listening ear, time alone, reassurance?

Expect that some requests will be met and others won't. A refusal is not necessarily a verdict on you. It may be about their capacity on that day. You can respond with disappointment and still keep the relationship.

Over time, people who ask clearly tend to find that their relationships become simpler. Others know where they stand, and the guessing game stops."""
),
(
"What Healthy Boundaries Can Actually Look Like", "relationships", 1, 52, False,
"Boundaries are often described as walls. In practice they are closer to clear, kind statements about what you can do.",
"A garden gate standing slightly open in a low stone wall",
"""The word boundary has taken on a slightly harsh tone online. It can sound like cutting people off. In everyday life, healthy boundaries are usually much quieter than that.

A boundary is information about what you can offer and what you can't. "I can't talk on the phone after nine, but I'd love to catch up on Saturday." "I'm not able to lend money, but I can help you look at your options." These are not rejections. They are a way of staying in a relationship without running yourself dry.

Boundaries tend to work best when they are stated calmly, before resentment has built, and when they describe your own actions and not the other person's. Instead of "You must stop calling me at work", try "I'm not able to take personal calls during work hours. I'll ring you back in the evening."

Some people will push against a new boundary, especially if the old pattern suited them. That is common, and it doesn't mean you were wrong to set it. Repeat it kindly and keep to it.

It is also worth recognising your own boundaries with yourself: how much you take on, how late you stay up, how often you say yes to things you resent.

If you are in a relationship where boundaries are routinely ignored or you feel afraid, please reach out to a trusted person or a specialist support service."""
),
(
"The Comfort of Being Understood", "relationships", 3, 79, False,
"Most of us do not need advice nearly as often as we need someone to understand.",
"Two people's hands around warm mugs on a wooden bench",
"""Think of the last time someone really understood what you were going through. They did not try to fix it. They said something like, "That sounds really hard," and it landed.

That feeling of being understood does something that advice rarely can. It lets the tension drop. It tells you that you are not strange for feeling as you do.

Most of us are tempted to jump in with solutions when a friend is struggling. It comes from a good place. But advice that arrives too quickly can feel like being told that the problem is simple, and that you should have thought of it.

Listening well is mostly about restraint. Let the person finish. Ask what it was like. Reflect back what you heard in your own words, and check that you have it right. Leave silences alone.

You can offer help afterwards, and it is often welcome if you ask first: "Would it be useful if I shared an idea, or do you mostly want me to listen?"

The same applies when we want to be understood ourselves. It is fair to say, "I don't need a solution right now. I'd just like you to hear it." Most people are relieved to know what is wanted.

Being understood does not make a problem disappear. It makes it easier to carry, and that is no small thing."""
),
(
"Why We Feel Guilty for Doing Nothing", "rest", 1, 14, False,
"Guilt over idleness is common and rarely helpful. Where it comes from and how to ease it.",
"A hammock strung between two trees in late light",
"""You sit down with nothing to do and, within minutes, a small voice says you should be doing something. The washing, the emails, the thing you said you would sort out.

That voice has a history. Many of us learned early that being useful earned approval. Over years, usefulness quietly became the measure of worth, and time spent not producing anything began to feel like a debt.

Modern life reinforces it. Our phones keep a running list of what is undone. Everyone seems to be doing more, or at least talking about it.

It may help to notice that rest is not the opposite of effort. It is part of how effort is sustained. Fields lie fallow, and muscles repair between sessions. People who rest properly tend to come back to their work with more attention.

You might try changing the label. Instead of "doing nothing", call it "recovering" or "making space". That may sound like a trick, but language shapes how we feel about an activity.

Another approach is to schedule it, which sounds clinical but works. A Sunday afternoon marked as free in your calendar is harder to give away to chores.

The guilt may still show up. You can let it sit there, acknowledge it, and rest anyway. It tends to quieten with repetition."""
),
(
"The Art of an Unhurried Morning", "rest", 0, 29, False,
"You do not need an hour. A few small choices can change the temperature of the first part of the day.",
"Morning sunlight on a bed with a book and a cup",
"""Mornings set a tone. If the first twenty minutes are a scramble for the phone and the door, the rest of the day can feel as if you are chasing it.

An unhurried morning does not need a long routine or an early alarm. It needs a little space, even ten minutes, where you are not responding to anyone.

A few things people find helpful. Leave the phone in another room overnight, so the first thing you see is not a notification. Prepare something the evening before, such as a bag by the door or clothes laid out. Open the curtains straight away and let light in.

Then choose one small pleasure. Making coffee properly, or standing at the window with your tea. Reading a few pages of a book. Stretching on the floor.

If you have children, a hard commute or a shift that begins early, this can look very different. Perhaps your unhurried moment is the shower, or the first sip of something hot before everyone else is up. Take what is possible.

The aim is not perfection. It is a bit of buffer between waking and the world's demands, so that you meet your day on your own terms, if only for a few minutes.

Try it for a week and see what changes. Often it is less about the morning itself than about what it says: today, I started on purpose."""
),
(
"Learning to Leave Some Things Unfinished", "rest", 3, 58, False,
"The list will never be empty. Practising stopping anyway.",
"A half-finished jigsaw puzzle on a table near a window",
"""There is a particular satisfaction in finishing. A cleared inbox, a tidy kitchen, a list with every line crossed through. It is a good feeling. It is also one that can quietly take over.

If we only allow ourselves to rest when everything is done, we will rarely rest, because the list refills. New emails arrive, the washing basket fills again.

Leaving things unfinished on purpose is a way of practising that your worth and your evening do not depend on completion. Stop the task at a natural pause, put a note on it for tomorrow, and walk away. The world is unlikely to end.

It can help to decide in advance what truly must be done today and what can wait. Most people find that the first list is much shorter than it feels. Write the must-do items first and treat the rest as optional.

There is a gentler side to this as well. Unfinished things can be pleasant. A book you pick up and put down for months. A garden project that evolves. A half-knitted scarf. Not everything has to be an achievement.

Try it as an experiment. One evening this week, leave one thing undone and notice what happens in your body. You may feel uneasy at first. That is normal. With practice, the unease tends to give way to something closer to relief."""
),
]
