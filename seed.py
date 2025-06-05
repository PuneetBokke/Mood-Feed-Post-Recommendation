from app import app, db
from models import Mood, Post
import os

# Ensure the instance folder exists (this is key!)
os.makedirs(app.instance_path, exist_ok=True)

with app.app_context():
    db.drop_all()
    db.create_all()

    happy = Mood(name='Happy')
    sad = Mood(name='Sad')
    excited = Mood(name='Excited')
    angry = Mood(name='Angry')
    calm = Mood(name= 'Calm')


    db.session.add_all([happy, sad, excited])
    db.session.commit()

    posts = [
        (Post(caption="Since I didn't generate an image of RCB (Royal Challengers Bangalore), I'll provide a caption for a hypothetical image: "
"RCB's fiery spirit takes center stage! The team's bold jersey and passionate fans create an electric atmosphere. Let's go RCB! #RCBForever #IPL",
image_url="images/happy1.jpg", mood=happy)
)
,
        Post(caption="Joyful moments etched in memory forever! Laughter, love, and adventure fill the air. Every smile, a treasure; every laugh, a gift. These happy memories warm the heart and lift the spirit. Cherishing life's precious moments, one smile at a time. Happiness abounds in every shared experience.", image_url="images/happy2.jpg", mood=happy),
        Post(caption="Sunshine on my face, happiness in my heart! A bright smile and a spring in my step, every day is a gift. Life's beauty is in the little things – a blooming flower, a warm breeze, or a good friend's company. Embracing each moment with joy and positivity, spreading happiness wherever I go.", image_url="images/happy3.jpg", mood=happy),
        Post(caption="Life's little pleasures bring immense joy! A good cup of coffee, a beautiful sunset, or a loved one's hug – happiness is in the details. Savoring each moment, big or small, fills the heart with delight. These joyful moments make life worth living, creating memories to cherish forever", image_url="images/happy4.jpg", mood=happy),
        Post(caption="Happy times are contagious! Laughter and smiles spread like wildfire, bringing people together. Whether big achievements or small victories, celebrating life's moments with joy and gratitude makes every day special. Sharing happiness with others multiplies its value, creating a ripple effect of positivity.", image_url="images/happy5.jpg", mood=happy),
        Post(caption="Picnic Fun", image_url="images/happy6.jpg", mood=happy),
        Post(caption="Pure happiness is a state of mind! Letting go of worries and embracing the present moment brings bliss. Finding joy in simplicity, beauty, and love fills the heart with contentment. This serene state of being is a treasure, radiating positivity and warmth to all around.", image_url="images/happy7.jpg", mood=happy),

        Post(caption="Sometimes, life's journey takes a melancholic turn. Tears fall, and the heart feels heavy. But even in sorrow, there's beauty – a chance to reflect, heal, and grow. Embracing emotions, allowing ourselves to feel, and finding solace in loved ones helps navigate life's challenges.", image_url="images/sad1.jpg", mood=sad),
        Post(caption="Ache of longing in the heart, yearning for what's lost. Memories linger, and the pain of absence is real. Yet, in this sadness, we find a way to appreciate what we had. Holding onto love and lessons learned, we move forward, carrying the memories with us", image_url="images/sad2.jpg", mood=sad),
        Post(caption="Lost in Thought", image_url="images/sad3.jpg", mood=sad),
        Post(caption="Sometimes, pain is too deep for words. Silent tears fall, and the heart feels overwhelmed. In these moments, it's okay to not be okay. Allowing ourselves to feel, seeking support from loved ones, and finding ways to cope helps heal the heart.", image_url="images/sad4.jpg", mood=sad),
        Post(caption="As the sun sets, shadows grow long, and the light fades. Sometimes, life's challenges make us feel like the light is slipping away. But even in darkness, there's hope – a chance to rest, recharge, and find our way again. Holding onto faith and loved ones helps navigate life's tough times.", image_url="images/sad5.jpg", mood=sad),


        Post(caption="The buzz of excitement is palpable! Every moment feels like a countdown to something amazing. The thrill of the unknown, the rush of adrenaline – it's exhilarating! Whether it's a new adventure or a milestone event, the anticipation builds, and the energy is infectious.", image_url="images/excited1.jpg", mood=excited),
        Post(caption="Leaping with joy, her excitement is palpable! Every moment is a celebration, every experience a gift. Her carefree spirit and infectious laughter spread happiness wherever she goes. Life's adventures are her playground, and she's ready to take on the world.", image_url="images/excited2.jpg", mood=excited),
        Post(caption="Life's too short to play it safe! Seeking thrills, embracing challenges, and pushing limits – that's the spirit! Every experience is a chance to grow, learn, and feel alive. The rush of excitement is addictive, and the memories last a lifetime.", image_url="images/excited3.jpg", mood=excited),
        Post(caption="The wait is almost over! Excitement builds, anticipation grows, and the energy is electric. Every moment feels like a countdown to something amazing. Whether it's a milestone event or a new adventure, the thrill of the experience is worth the wait", image_url="images/excited4.jpg", mood=excited),

        Post(caption="Flames of fury burning bright! Anger seethes beneath the surface, ready to erupt. Every word, a spark; every action, a firework. The storm rages on, fueled by intense emotions. A moment of calm is all it takes to tame the beast, but for now, the fire burns.", image_url="images/angry1.jpg", mood=angry),
        Post(caption="Stormy temper, a whirlwind of emotions! Her anger is a force to be reckoned with, intense and unbridled. Every glance is a lightning bolt, every word a thunderclap. Her feelings are raw and real, a testament to the power of human emotion. A calm breeze is all it takes to soothe the storm, but for now, it rages on", image_url="images/angry2.jpg", mood=angry),
        Post(caption="Fierce emotions blaze in her eyes! Anger and frustration seethe beneath the surface, ready to erupt. Every glance is a spark, every word a flame. Her intensity is palpable, a whirlwind of feelings that's hard to ignore. A moment of calm is all it takes to tame the storm, but for now, her emotions rage on.", image_url="images/angry3.jpg", mood=angry),

        Post(caption="Serenity found amidst majestic mountains! The calm atmosphere and breathtaking view soothe the soul. Peaceful moments like these remind us to breathe, reflect, and recharge. Nature's grandeur has a way of calming the mind and lifting the spirit.", image_url="images/calm1.jpg", mood=calm),
        Post(caption="Tranquility by the water's edge! The gentle ripples and soothing sounds calm the mind. Peaceful moments like these bring clarity and serenity, washing away worries and stress. The beauty of nature has a way of healing the soul.", image_url="images/calm2.jpg", mood=calm),
        Post(caption="Reflections of serenity on calm waters! The gentle lapping of waves against the shore, the soft rustle of reeds – nature's symphony soothes the soul. A moment of peace, a lifetime of memories. The water's edge, where calmness meets beauty.", image_url="images/calm3.jpg", mood=calm),
        

    ]

    db.session.add_all(posts)
    db.session.commit()
