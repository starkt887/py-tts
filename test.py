from gtts import gTTS
import gtts
# This module is imported so that we can do some os operations
import os

# print(gtts.lang.tts_langs())

language = 'hi'

try:

    
    # The text that you want to convert to audio
    myobj = gTTS(text="शुरुआती दृश्य न्यूयॉर्क के मोंटौक में सेट किया गया है, जहाँ गैरी नाम का एक टो ट्रक चालक अपनी पूर्व प्रेमिका मैडी के घर उसकी कार छीनने के लिए आता है। यह पता चलता है कि उसकी कार को जब्त किया जा रहा है क्योंकि उसे अपनी माँ से विरासत में मिले घर पर संपत्ति कर देना है। मैडी दो नौकरियाँ करती है, एक बारटेंडर की और दूसरी उबर ड्राइवर की, और अपनी कार खोने का मतलब है उबर ड्राइवर के रूप में काम करने की उसकी क्षमता खोना। नतीजतन, वह गैरी को अपनी कार छोड़ने के लिए मनाने की कोशिश करती है। वह उसकी भावनाओं को भी लुभाने की कोशिश करती है, लेकिन उसके प्रयासों को एक अन्य व्यक्ति द्वारा बर्बाद कर दिया जाता है, जिसके साथ उसने पिछली रात संबंध बनाए थे। यह देखकर, गैरी उसकी कार को अपने टो ट्रक से बांधता है और चला जाता है। अब कार रहित, मैडी काम पर जाने के लिए रोलरब्लेडिंग का सहारा लेती है। रास्ते में, वह एक कॉफ़ी शॉप के बाहर खड़ी गैरी की टो ट्रक को देखती है। यह देखकर कि वह अंदर व्यस्त है, मैडी जल्दी से अपनी कार खोलती है और भागने की कोशिश करती है। हालांकि, वह भूल जाती है कि यह ट्रक से बंधा हुआ है। इसके परिणामस्वरूप एक छोटा सा हंगामा होता है, और गैरी जल्दी से घटनास्थल पर पहुंचता है और कार को वापस ऊपर उठाता है। मैडी अपने कार्यों के परिणामस्वरूप परिवीक्षा पर समाप्त होती है, लेकिन शुक्र है कि उसे गेब नामक उसके दोस्त द्वारा जमानत मिल जाती है। इसके बाद, मैडी एक बार में अपनी नौकरी के लिए भागती है, उसकी हताशा अभी भी बनी हुई है। वह तब और अधिक परेशान हो जाती है जब एक ग्राहक बार के आधिकारिक रूप से खुलने से पहले एक ड्रिंक की मांग करता है। परिणामस्वरूप, वह ग्राहक के साथ बहस में पड़ जाती है, जिसके कारण उसे अपने प्रबंधक, फर्न से डांट पड़ती है। फर्न फिर मैडी को नैपकिन मोड़ने का काम सौंपती है। वहाँ, उसके साथ उसकी गर्भवती सहकर्मी, सारा और उसका पति, जिम भी होते हैं। जब तीनों गपशप करते हैं, तो सारा उसे अमीर क्रिप्टोकरेंसी निवेशकों, बेकर्स से एक अजीबोगरीब नौकरी का अवसर दिखाती है। वे वर्तमान में अपने अंतर्मुखी 19 वर्षीय बेटे, पर्सी के साथ डेट करने के लिए किसी की तलाश कर रहे हैं, और बदले में, वे मुआवजे के रूप में अपनी ब्यूक रीगल कार की पेशकश कर रहे हैं। घर खोने से बचने के लिए बेताब, मैडी इस असामान्य क्रेगलिस्ट पोस्टिंग को स्वीकार करने का फैसला करती है। अगले दिन, वह नौकरी पर चर्चा करने के लिए अमीर माता-पिता के घर जाती है। माता-पिता: लेयर्ड और एलिसन उसे अपने बेटे के बारे में बताते हैं, जो शर्मीला है और उसे लड़कियों, शराब पीने, पार्टियों या सेक्स का कोई अनुभव नहीं है। वे उसके शरद ऋतु में प्रिंसटन विश्वविद्यालय में जाने से पहले उसका आत्मविश्वास बढ़ाने की उम्मीद करते हैं। जैसे-जैसे उनकी चर्चा आगे बढ़ती है, जोड़ी को पता चलता है कि मैडी पहले से ही 32 वर्ष की है, जिससे वे कुछ हद तक हिचकिचाते हैं। बहरहाल, मैडी का दावा है कि उन्हें वास्तव में एक युवा लड़की की नहीं बल्कि किसी परिपक्व व्यक्ति की जरूरत है जो उनके बेटे को एक जिम्मेदार आदमी बनने की दिशा में मार्गदर्शन कर सके।", lang=language, slow=False)
    myobj.save(f"hinditest.mp3")
    # export to mp3
    os.system(f"start hinditest.mp3")
except:
    print("something went wrong!")
