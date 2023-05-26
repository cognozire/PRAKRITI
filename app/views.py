from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
# Create your views here.

def index(request):
    return render(request,'app/index.html')

def dosh(request):
    return render(request,'app/dosh.html')

def disease(request):
    return render(request,'app/diseases.html')

def diet(request):
    return render(request,'app/diet.html')

def asana(request):
    return render(request,'app/asana.html')
def anasa1(request):
    return render(request,'app/anasa1.html')

def y_asana(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
    diff_conc = ['Siddhasana','Bhadrasana','Shavasana']
    if name == 'Difficulty in Concentration':
        y_asana = diff_conc
    tremors = ['Kukkutasana','Tolangulasana']
    if name == 'Tremors':
        y_asana = tremors
    context = {'y_asana': y_asana}
    return render(request,'app/y_asana.html',context)

def result(request):
    
    vata=0
    pitta=0
    kapha=0
    question = ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19']
    # logic for code
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        for ques in question:
            prakriti = request.POST[ques]
            if (prakriti=='VATA'):
                vata=vata+1
            if (prakriti =='PITTA'):
                pitta=pitta+1
            if (prakriti == 'KAPHA'):
                kapha = kapha+1
    
    
    
    if (vata>pitta and vata>pitta):
        class_type = 'vata'
    elif(pitta>kapha):
        class_type = 'pitta'
    else:
        class_type = 'kapha'
    context = {'class_type':class_type}
    
    return render(request,'app/result.html',context)




def result3(request):
    diseases_pitta = [
            "Heat generation in body",
"Acid Reflux",
"Indigestion",
"Inflammation of joints",
"Skin allergies",
"Stomach ulcers",
"Gall-bladder and liver disorder",
"Sciatica",
"Arthritis",
"Menstrual disorders"
        ]
    diseases_kapha =["Cold, cough", "seasonal allergies",
"Bloating in stomach/indigestion",
"Obesity",
"Depression",
"Thyroid",
"Cataract/ocular diseases",
"Diabetes",
"Asthma",
"Lethargy/fatigue",
"Pulmonary diseases",
        ]
    diseases_vata = ["Rough Skin",
"Hyper-pigmentation",
"Flatulence/Gastric",
"Muscle Spasms",
"Asthma",
"WeightLoss",
"Constipation",
"Insomnia",
"Cramps",
"Pelvic pain",
"Hoarseness of voice",
"Toothache",
"Deafness",
"Headache",
"Dandruff",
"Tremors",
"Difficulty in concentration"
]




    if request.method == 'POST':
        name = request.POST['name']
    if(name == 'vata'):
        diseases = diseases_vata
    if(name == 'pitta'):
        diseases = diseases_pitta
    if(name == 'kapha'):
        diseases =diseases_kapha
    
    
    context = {'diseases':diseases}
    

    if(name == 'vata'):
        print("1")
        return render(request,'app/result3.html',context)
    if(name == 'pitta'):
        print("2")
        return render(request,'app/pitta_dis.html',context)
    if(name == 'kapha'):
        print("3")
        return render(request,'app/kapha_dis.html',context)


def result2(request):
    
    # logic for code
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
       
    if (name=='pitta'):
        data_pitta = {
            'Embrace':['slow','steady','small shift'],
            'Flavour':['coolover',
'warm or hot',	
'dense grounding and nourishing',	
],
            'Emphasize':['sweet',
'bitter',
'astringent'
],
            'Minimize':['sweet','sour','salty'],
           
        }
        data_pitta_df = pd.DataFrame(data_pitta)
        df_pitta = {"Early Morning":["Jeera + coriander + fennel water",
"Jeera + coriander + fennelwater",
"Jeera + coriander + fennelwater",
"Jeera + coriander + fennelwater",
"Jeera + coriander + fennelwater",
"Jeera + coriander + fennelwater",
"Jeera + coriander + fennelwater",
"Jeera + coriander + fennel water",
"Jeera + coriander + fennel water",
"Jeera + coriander + fennel water",
],"BreakFast":["a. Egg whites and vegetable omlete b. Dates and almond shake",
"Vegetable poha+green chutney",
"Vegetable upma+green chutney",
"Vegetable oats",
"Vava idli+coconut chutney",
"Vegetable sandwich",
"Besan chilla+chutney",
"Baneer cutlettes+chutney",
"Rice dhokla+green chutney",
"Egg whites",
],"Mid-Morning":['05 Soaked almond+1walnut',
"01 Apple",
"Fruit chaat",
"01 Bowl papaya",
"01 Apple",
"01 Bowl pomegranate",
"01 Apple",
"01 Apple + 01 Kiwi",
"01 Banana",
"01 Apple + 01 Kiwi",
],"Lunch":["Cabbage + whole wheat roto",
"Black chana chaat",
"Ladyfinger vegetable+oats roti + curd + cucumber salad",
"Quinoa khichdi",
"Vegetsbles rawa uttpam + chutney",
"Mix veg + whole wheat roti + curd + salad",
"Missi roti(50 besan+50 whole wheat atta)",
"Paneer curry + roti + salad",
"Dal + rice + cucumber salad",
"Chicken curry + whole wheat roti",
],"evening":["Roasted makhana + fennel tea",
"Bhel + green tea",
"Roasted murmura + green tea",
"05 Soaked almonds +01 walnut",
"Roasted murmura + green tea",
"Roasted makhana + green tea",
"Bhel + green tea",
"Roasted murmura",
"Bhel",
"Roasted murmura",
],"Dinner":["Pumpkin soup",
"Ghiya soup",
"Sprouts",
"Milk + museli",
"01 Bowl moong dal",
"01 Bowl sauted vegetables",
"Dal soup",
"100 gms paneer tikka",
"01 Bowl dal",
"Chicken tikka",
]}
        df_pitta_diet= pd.DataFrame(df_pitta)
        context = {'class_type':name,'DataFrame_Vata': data_pitta_df,'DataFrame_vata_diet':df_pitta_diet}


    if(name=='kapha'):
        data_kapha = {
            'Embrace':['slow','steady','small shift'],
            'Flavour':['light and airover',
'dense and haevy',	
'warm over cool',	
],
            'Emphasize':['pungent',
'bitter',
'astringent'
],
            'Minimize':['sweet','sour','salty'],
            'prone-to':['tonsillits',
'sinusitis',
'bronchitis',

]
        }

        data_kapha_df = pd.DataFrame(data_kapha)



        df_kapha = {'BREAKFAST':
['vegetable oats upma+tea',
'1 glass fruit smoothie',
'rice idli with greenchutney',
'vegetable poha',
'dhokla+mint chutney',
'oats upma',
'egg white omellette',
'fruit smoothie',
'museli+milk',
'vegtable poha'],
'Mid-Morning':['fruit salad ( apple+cherries+kiwi)',
'2-3soaked figs',
'vegetable juice',
'fruit salad',
'buttermilk',
'soaked figs',
'soaked almonds(5-6)+ 1 walnut',
'vegetable juice',
'papaya',
'pomegranate',
],
'LUNCH':['yellow moond dal chilla + green chutney',
'quinoa roti+green vegetables salad',
'mix dal chilla+green chutney',
'kala chana chaat',
'brown rice pulao+vegetable raita',
'oats chilla + tomato onion raita',
'quinoa roti+egg bhurji+salad',
'whitechana chaat',
' mix dal chilla+green chutney',
'kala chana salad'],

'SNACKS':['roasted chana+green tea',
'roasted peanuts+ jasmine tea',
'roasted peanuts+jasmine tea',
'wheat khakra+jasmine tea',
'roasted chana+jasmine tea',
'roasted murmura+jasmine tea',
'roasted mix grains+green tea',
'roasted mix grain+tea',
'roasted makhana+jasmine tea',
'roasted moong+jasmine tea'],

'Dinner':['oats+milk',
'lentil soup',
'almond milk shake',
'museli+milk',
'cereal+ milk',
'museli+milk',
'grilled chicken+vegetable',
'dal daliya',
'stir fry vegetables',
'wheatflakes+milk'
]





        }
        
        df_kaphadiet= pd.DataFrame(df_kapha)
        context = {'class_type':name,'DataFrame_Vata': data_kapha_df,'DataFrame_vata_diet':df_kaphadiet}
        

    
    
       
    if(name=='vata'):
        data_vata = {
                    'Embrace':['Slow','Steady','SmallShift','NULL'],
                    'Favour':['Warm over cold','Moist and oily over dry','Grounding Nourishing stabilizing','NULL'],
                    'Emphasize':['Sweet','Sour','Salty','NULL'],
                    'Minimize':['pungent','Bitter','Astringent','NULL'],
                    'Prone_to':['Gas','backPain','Sciatica','Joint-Inflammation']}
        
        df_vata = pd.DataFrame(data_vata)
        print(df_vata)
        Vata_diet = {
            'breakfast':['Vegetable Upma + Green Chutney',
'Fruit Smoothie + Pinch of Cinamon powder',
'Vegetable Poha', 
'Rice Idli + Coconut Chutney',
'Besan Dhokla + Green Chutney',
'Fruit Smoothie',
'Vegetable Sandwich',
'Moon Dal Chilla + Green Chutney',
'Vegetable Vermicelli',
'02 Egg Whites'
],
'Mid-Morning':['01 Apple',
'Pomegrenade',
'Fruit Salad',
'01 Apple',
'Buttermilk',
'Soaked Figs',
'Vegetable Juice',
'01 Apple',
'01 Guava',
'01 Apple'
],
'lunch':['Moon Dal Chilla + Chutney + Salad',
'Brown Rice + Vegetable Pulao + Cucumber Raita',
'Quinoa Roti + Green vegetables + Salad',
'Plain Dosa + Sambar + Chutney',
'Onion Missi Roti + Onion Tomato Raita',
'Boiled White Chana Chat',
'Sauted Vegetables + Whole Wheat Roti + Yogurt',
'Yellow Moon Dal + Brown Rice + Salad',
'Ghiya + Oats Roti + Salad',
'Quinoa Roti + Egg Bhurji + Salad'
],
'Snack':['Roasted Peanuts + Green Tea',
'5-6 Almonds + 01 Wallnut',
'Roasted Grains + Green Tea',
'Roasted Makhana + Green Tea',
'Roasted Grains + Green Tea',
'5-6 Almonds + 01 Wallnut',
'Roasted Murmura + Green Tea',
'Murmura Bhel',
'Roasted Peanuts + Green Tea',
'Roasted Murmura + Green Tea',
],
'Dinner':['Milk + Oats',
'Milk + Museli',
'Sauted Vegetables',
'Milk + Museli',
'Lentil Soup',
'Ghiya Soup',
'Milk Daliya',
'Milk + Wheat Flakes',
'Milk + Oats',
'Chicken Tikka'
]

        }
        df_vatadiet= pd.DataFrame(Vata_diet)
        context = {'class_type':name,'DataFrame_Vata': df_vata,'DataFrame_vata_diet':df_vatadiet}

    
    return render(request,'app/result2.html',context)