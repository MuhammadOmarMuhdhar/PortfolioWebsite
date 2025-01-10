import streamlit as st
import json  

# Blog data with titles, dates, summaries, and content
blogs = [
    {
        "id": "large-language-models",  # Unique ID for query parameter linking
        "title": "Are Large Language Models Just Fancy Chatbots?",
        "date": "December 24, 2024",
        "summary": "Chatbots are just the beginning of what large language models can do.",
        "content": """
    Artificial intelligence (AI) is no longer just a concept in science fiction, it is real and already affecting people’s daily life. The manner that it exists is vastly different from the robot-filled stories we believed as children. Rather than an anthropomorphic entity, artificial intelligence exists largely behind the scenes, hidden in data centers and algorithms that operate away from public view. 
    
    One of the most accessible and recognizable applications of AI is large language models (LLMs), which power tools like ChatGPT and similar chatbots. For many, these chatbots represent their most direct interaction with AI. Since their launch, these tools have experienced explosive growth in adoption. By February 2024, [20% of Americans reported using ChatGPT](https://www.pewresearch.org/short-reads/2024/03/26/americans-use-of-chatgpt-is-ticking-up-but-few-trust-its-election-information/#:~:text=The%20share%20of%20employed%20Americans,or%20for%20entertainment%20(17%25).). Its versatility is evident in its wide-ranging applications—30% of adults have leveraged it for work-related tasks, such as drafting emails, generating reports, and brainstorming creative ideas.

    While these models have been embraced and widely adopted, their sophistication and significance as artificial intelligence are often underappreciated. A common critique dismisses large language models as nothing more than advanced text prediction algorithms. While technically accurate, this characterization fails to capture the remarkable complexity and innovation behind their design.

    Consider this thought experiment: present a well-read English speaker with a sentence containing an unfamiliar word. More often than not, they can infer its meaning with a high level of accuracy just from the context. This ability stems from the intricate patterns and relationships that exist within language, patterns learned and internalized through years of reading, communication, and cultural immersion.

    The remarkable achievement of large language models is that, in their own way, they mirror this human capacity. The neural networks behind these models are able to process vast amounts of text and internalize their linguistic structure. Likewise, when these models encounter a sentence with a word they’ve never seen before, they can deduce its likely meaning from contextual cues. Like humans, these models don’t simply make mechanical predictions; instead, they synthesize information to achieve what can be described as a contextually relevant understanding.

    Chatbots are currently the most familiar example of this technology in action, but they’re only scratching the surface of what’s possible.

    """
    },
    {
        "id": "determinism-as-a-politic", 
        "title": "Determinism as a Politic",
        "date": "November 12, 2024",
        "summary": "Reflections on my political worldview",
        "content": """
    Eight years ago, November 2016, I recall the chaos of Trump's first victory. I was 16 and it felt like the world was about to end. I remember getting into so many heated conversations with my classmates in my Texas high school. Most of them were Republican just to be edgy, being contrarian just because. Trump was obviously a con man who only cared about himself, and he was going to destroy everything. I saw that even at 16. Yeah, Hillary Clinton sucked, but she was infinitely better than Trump. And I argued this back and forth with my classmates.

    Eight years later, I find myself in a similar position, though now it's more of a lukewarm conversation than heated, with my peers in my mid-20s. But something's different this time. I'm not the one emotionally affected by Trump's campaign – it's my peers who are, and they are shocked, maybe even concerned that I’m not. To be clear: my opinion of Trump hasn't changed. He's still a dangerous con man. And Kamala, like Hillary before her, might not be great, but she's better than Trump. Yet somehow, even as a Muslim named Muhammad, in a time when Trump built his platform on Islamophobia, I can't bring myself to feel that same concern that I once did.

    I'm writing this today to understand myself better. While my political ideology has fundamentally stayed the same, my emotional response to politics has changed, and I want to understand why.

    My political awakening began with Trayvon Martin's murder in 2012. This is significant, to roughly quote John Lewis, Trayvon Martin was to us what Emmett Till was for his generation – the generation of the Civil Rights movement. It was my second year in the United States, and this is when I began to understand the deep social stratification of American society. Then came 2016, not just the year of Trump, but the year of Bernie Sanders, who introduced me to the politics of hope. He represented the idea that a better world wasn’t just possible; it was something we could work together to create. I’ll never forget the iconic moment when a bird landed on his podium mid-speech, almost like nature itself was affirming this world view.

    This hopeful outlook shaped my politics until 2021, another pivotal year, marked by the murder of George Floyd and the turmoil of the COVID-19 pandemic. Oddly enough, despite everything, I’d never felt more optimistic. Society’s reaction to Floyd’s murder and the ensuing social unrest felt like a turning point. If Trayvon Martin was our generation’s Emmett Till, then this was our Civil Rights movement. The world seemed to be moving toward change, and my hope felt justified.

    I was deeply invested in this movement, both emotionally and through my active involvement at the university level. As part of a student organization advocating for Black students, I felt like I was playing a role in something larger, almost like being part of the SNCC. I didn’t see myself as Kwame Ture (Stokely Carmichael) or John Lewis—not in fame or legend—but as a member of a movement. I may not be remembered by history, but I was part of it.

    So you can imagine how I felt when a year later, the movement had completely fizzled out and nothing had changed. The Black Lives Matter movement ended with embezzlement scandals, my own student activism led nowhere, and the main political “win” was replacing Trump with Joe Biden. Joe Biden—the author of the 1994 crime bill. Biden, who told us that not voting for him meant we weren't Black. Biden, who once called desegregation policies a “racial jungle,” who opposed Medicare for All in a pandemic. Joe Biden—the white moderate Martin Luther King and Malcolm X warned us about.

    Simultaneously, my studies introduced me to a field that fundamentally reshaped how I viewed the world: the philosophy of science. In particular, I became obsessed with Darwinism, not in the traditional sense of evolution and biology, but as a worldview. According to the concept of natural selection, every facet of life unfolds not by intention but through relentless, impersonal processes governed by the unconscious hand of nature. This concept, known as scientific determinism, challenged everything I thought I understood about progress and society.

    Where I once believed in the power of human will and morality to drive meaningful change, I began to see societal development as an inevitable outcome of forces beyond our control, dictated by natural laws as indifferent as evolution itself. If this is true, if all human actions are governed by forces as indifferent as natural selection, how meaningful, then, is the pursuit of progress? How much of what we strive to change is truly within our control?

    These questions brought me an unexpected sense of relief. Believing that larger forces shape our outcomes helped me release the anxiety and disappointment that underpinned my political and social ideals. This worldview aligned with the detachment I was already beginning to feel, providing a rationale for my growing disillusionment. If every aspect of life is ultimately molded by forces beyond our control, perhaps caring less isn’t a moral failing but rather an acceptance of reality. Embracing determinism allowed me to set down the burdens of idealism and adopt a quieter, less anxious perspective on the world.

    To some, this shift might seem like nihilism, a surrender of meaning or purpose. But for me, it wasn’t about giving up on life or disengaging from the world. Instead, it was about recognizing the limits of control and learning to live within them. This perspective didn’t strip life of purpose; it simply redirected it to focus on the one thing I could change: myself.

    A year after undergrad, I began working to address a lifelong speech impediment that had always held me back. I stopped chronically smoking weed and committed to building a solid work ethic. I established a consistent hygiene routine, became intentional about my physical health, and structured my days around time for reflection and personal growth. I recognized that while I couldn’t make the world a better place, I could strengthen myself to better navigate a world that is, by nature, unpredictable and beyond my control.

    Life was getting better. Slowly but steadily, my efforts began to bear fruit. The speech impediment that had defined so much of my life was affecting me less, and I had adopted a worldview that gave me control.

    Some might say I have the privilege to accept this view, to find comfort in detachment. I disagree. As Marx famously observed, religion is the opium of the masses. For many, religion offers the solace that I found in scientific determinism, the relief that comes from accepting that the course of society is not in our hands. Marx himself believed in a kind of determinism, scientific socialism, where he saw class struggle as a driving force propelling society toward an inevitable socialist future.

    My belief in determinism diverges from his framework. I don’t see history as moving along a set course, nor do I see any inevitable end goal for society. Rather, my determinism is retrospective, something I observe in hindsight. History, as I see it, is less a purposeful journey and more a series of chaotic forces, events, and competing interests that can only be fully understood after they’ve unfolded.

    This perspective shapes how I interpret Donald Trump’s decisive victory over Kamala Harris and the Republicans’ sweeping triumph over Democrats in the 2024 election. Before, I couldn’t have predicted it; but looking back now, it feels inevitable. America’s decline has been a long time coming. Our social infrastructure—our healthcare system, our education system, our basic social safety nets—has been eroding for decades, leaving millions vulnerable and disillusioned. As inequality has widened and working-class support systems have deteriorated, Americans have become increasingly desperate for change.

    The Democratic Party, supposedly the bastion of progressive ideals, has repeatedly sabotaged movements that might address these root issues. Even in moments when change seemed within reach, we’ve seen Democratic leaders actively undermine progressive candidates and policy initiatives to preserve their own power and maintain the status quo. Calls for universal healthcare, student debt cancellation, and fair wages are dismissed as “unrealistic” or “too radical,” effectively sidelining the very reforms that could begin to heal the country’s structural wounds.

    In hindsight, Trump’s return to power seems almost a natural consequence of this betrayal. As Bernie Sanders pointed out, the Democrats’ reluctance to support real, substantive reforms has fueled resentment among voters who feel abandoned. This disillusionment has driven people to either disengage entirely or swing toward a party that, for all its flaws, at least claims to reject the establishment.

    Looking back on 2016, I remember the fervor and certainty that my arguments could sway minds, that the right choice was clear. I believed that reason and logic had the ability to guide the world.

    Now, in 2024, the situation feels familiar, yet my emotional response is different. Trump’s resurgence and Harris’s defeat neither shocked nor saddened me; they felt like the predictable outcome of momentum that has been building for years. The calm my peers notice isn’t apathy; it’s acceptance. I still hold the same ideals I did in 2016, but I now see history less as a tale of heroes and villains and more as a series of events. Trump’s return isn’t a cause but a consequence of the society we inhabit, a cycle of cause and effect, of actions and reactions.

    In many ways, my worldview has only been reinforced over time, but it now faces its greatest test. While I may not have absolute control of my outcomes, I can still position myself in ways that align with my goals. I can make choices and build habits that, in my view, increase the chances of reaching my desired outcomes, even if they don’t guarantee them. If Trump’s return brings the turmoil that we anticipate, then, by God’s will—and if my worldview holds true and I act accordingly—I’ll be able to shield myself and those I care about. And if I cannot, then I will face that challenge when it arrives. Ultimately, I have to bet on myself because that’s the only thing I truly have any control over.

    So this isn’t a rejection of hope or a descent into fatalism; in fact, it’s quite the opposite. It’s the belief that, even within the limits of human control, there is still something I can do. My ideals remain intact, but my approach is more inward, and, in my view, more grounded in reality.
    """
    },
    {
        "id": "nostalgia-for-boredom",  
        "title": "Nostalgia for Boredom",
        "date": "April 16, 2024",
        "summary": "The lost art of doing nothing.",
        "content": """
    I’m a part of the older end of the Gen Z spectrum, I’m 24, which means I have some recollection of a period before the Internet took over as a central part of our existence. My memories of this pre-internet world are somewhat fleeting, but they still evoke a sense of nostalgia. I remember enough to enable me to draw comparisons between life back then and the digital age we live in today. I remember the excitement of waiting for my favorite TV show to air at a specific time each week and the small joys of playing outside, exploring the neighborhood with friends. These memories, although hazy, serve as a reminder of how much our world has evolved, and as I transition into adulthood, these memories have led me to reflect on the ways the Internet has reshaped our daily experiences. I’ve found myself asking, am I ok with this? Am I ok with how the world has changed?

    As Gen Z, we are truly the first ‘internet generation’, some of my younger peers genuinely can’t remember what life was like before the internet. The internet has changed many things about how we live, like how we think and interact with others. One reason for this is due to the fact that it’s an unlimited resource. When we're online, we can access all sorts of information, media, music, and more without any end. This kind of endless access is new and different for us humans. Our behaviors and characteristics evolved in an environment of scarcity. Before the late 20th century, most people in any society were not familiar with abundance, let alone limitless abundance. Our minds aren't used to things having no limits; our brains don’t even have the capabilities to fully conceptualize or imagine something that is unlimited. This prompts a compelling question: how does a species that is conditioned to finite resources behave when exposed to an infinite resource?

    I don't possess the expertise necessary to tackle this question comprehensively. Instead I want to focus on a specific aspect of our daily lives that has been profoundly altered by the internet – boredom, and specifically, our relationship with it. In a reality where access to stimuli has no bounds, can we even experience boredom?

    Boredom, in the most simple way to describe it, is when your mind is completely idle. It is a state of being in which your brain is not receiving any type of stimulation, where you are experiencing nothing.  As a child, before I discovered what the internet was, I recall constantly being bored. These memories are described well with Mark Fisher’s words in the article No One is Bored, Everything is Boring. In this article Mark Fisher recalls boredom that was caused by “the dreary void of Sundays, the night hours after television stopped broadcasting, even the endless dragging minutes waiting in queues [smartphones didn’t exist to occupy this time].” Today this type of boredom isn’t possible, because when we’re in lines waiting, we have our phones to stimulate our minds. We rarely have moments when our minds are completely idle. 

    Mark Fisher explains that boredom acts as a motivating agent. When someone is experiencing complete idleness, the feeling of nothing, they seek ways to alleviate it by finding something more engaging or stimulating to do. “The vacancy of boredom was a challenge, an injunction and an opportunity:’ he writes, “if we are bored, then it is for us to produce something that will fill up the space.”

    Extrapolating on this thought, Mark’s words implies that boredom creates a reward cycle in your brain that motivates you to want to do things. The feeling of nothingness triggers a drop in dopamine levels as a lack of stimulation is perceived. To counteract this feeling of nothing, you set and complete tasks,  activating the brain's reward system by releasing dopamine.  The anticipation, progress, and eventual completion of tasks form a cycle where dopamine release becomes associated with overcoming the feeling of nothing, motivating future engagement in similar activities.

    “In the intensive, 24/7 environment of capitalist cyberspace” Mark Fisher writes, “ the brain is no longer allowed any time to idle; instead, it is inundated with a seamless flow of low-level stimulus.” 

    However, despite experiencing constant stimulation, of course boredom is still a phenomenon that exists. I find myself feeling bored frequently, and I'm sure many others do too. This means how we experience, and consequently the definition of, boredom has changed.

    This evolution in our experience of boredom can be compared to the experience of over-eating your favorite food. When you consume your favorite food only occasionally, you look forward to it and are even excited about the opportunity to eat it. However, if you begin to eat it every day, the excitement associated with it diminishes; as there is nothing particularly special about it anymore. This parallels the impact that living within a "24/7 environment of capitalist cyberspace" has had on our experience of dopamine. 

    Our limitless exposure to stimuli has had a numbing effect on the feeling of dopamine. The fact that our brains didn't have constant access to it is what made dopamine feel like a reward when we did experience it. In other words, in a world where we are constantly stimulated,  the sensation of being stimulated itself becomes boring. Consequently, the incentive cycle beginning with feeling bored that motivates action, loses its effectiveness. Further perpetuating the feeling of boredom.

    Once upon a time boredom used to be a means to an end. Our minds created a reward cycle that leveraged the feeling of nothingness to cause action. Today, boredom is itself an end. In this modern era where we have access to unlimited stimuli, via the internet, we are stuck in an almost constant state of boredom. Amidst our daily routines, our lives are saturated with patterns that are repetitive and boring, yet our nervous systems remain in a state of constant arousal. Even once we acknowledge the mundane nature of aimlessly scrolling on Tik Tok, listening to our current favorite songs on loop, reading people's opinions on twitter topics that we have no genuine interest in; we find ourselves irresistibly drawn to repeat these tasks. This leaves us devoid of the opportunity to truly experience nothing, an experience that once used to play an important role in the daily lives of humans. 
     """
    },
]

with open("blogs.json", "w", encoding="utf-8") as f:
    json.dump(blogs, f, ensure_ascii=False, indent=4)