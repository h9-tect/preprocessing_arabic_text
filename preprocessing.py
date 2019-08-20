#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script handles cleaning arabic tweets using some of the commonly known arabic preprocessing techniques starting.

import re
import pyarabic.araby as araby

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# test sample
tweet1 = u'جهود تُبذل عامًا بعد عام تعبّر عن ترابط الجسد الواحد لخدمة ضيوف الرحمن؛ تطبيق ترجمان الفائز في #هاكاثون_الحج العام الماضي، ينطلق اليوم ليشارك الحجاج أيامهم الروحانية ويساعدهم في ترجمة اللوح الإرشادية في منطقة الحرم دون الحاجة إلى انترنت @reem. #حج_ذكي'



# removes usernames inside a tweet text caused by to mentions or reply tweets
def remove_usernames(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)

    return input_txt

# removes arabic letters tashkeel like (ِ ًٍ ٌ  ّ ْ )
def remove_tashkeel(input_txt):
    return araby.strip_tashkeel(input_txt)

# removes a decorative letter (ـ) which has no affect on words meaning
def remove_tatweel(input_txt):
    return araby.strip_tatweel(input_txt)

# normalizes the different forms of the letter hamza (ئ ؤ) into a single form (ء)
def normalize_hamza(input_txt):
    r = re.findall(u'ئ',input_txt);
    e = re.findall(u'ؤ',input_txt);
    for i in r:
        input_txt= re.sub(i, u'ء', input_txt)
    for i in e:
        input_txt= re.sub(i, u'ء', input_txt)
    return input_txt

# normalizes the different forms of the letter alef (آ أ إ) into a single form (ا)
def normalize_alef(input_txt):
    r = re.findall(u'أ',input_txt);
    e = re.findall(u'إ',input_txt);
    o = re.findall(u'آ', input_txt);
    for i in r:
        input_txt= re.sub(i, u'ا', input_txt)
    for i in e:
        input_txt= re.sub(i, u'ا', input_txt)
    for i in o:
        input_txt= re.sub(i, u'ا', input_txt)
    return input_txt

# normalizes the different forms of the letter yeh (ي ى) into a single form (ى)
def normalize_yeh(input_txt):
    r = re.findall(u'ي', input_txt)
    for i in r:
        input_txt = re.sub(i, u'ى', input_txt)
    return input_txt

# normalizes the different forms of the letter heh (ه ة) into a single form (ة)
def normalize_heh(input_txt):
    r = re.findall(u'ه', input_txt)
    for i in r:
        input_txt = re.sub(i, u'ة', input_txt)
    return input_txt

# combining all preprocessing functions together for testing samples
def full_preprocessing_steps(tweet):

    print("Tweet before preprocessing: " + tweet)

    usernames_free = remove_usernames(tweet,  "@[\w]*")
    tashkeel_free = remove_tashkeel(usernames_free)
    tatweel_free = remove_tatweel(tashkeel_free)
    hamza_normalized = normalize_hamza(tatweel_free)
    alef_normalized = normalize_alef(hamza_normalized)
    yeh_normalized = normalize_yeh(alef_normalized)
    heh_normalized = normalize_heh(yeh_normalized)

    print("Tweet after preprocessing: " + heh_normalized)

full_preprocessing_steps(tweet1)