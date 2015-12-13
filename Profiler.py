__author__ = 'chintanpanchamia'
import csv
record = open('record.csv','a')
csvwriter1 = csv.writer(record)

agreeableness = 0
agreeableness_counter = 0
agreeableness_reverse = 0
agreeableness_reverse_counter = 0

conscientiousness = 0
conscientiousness_counter = 0
conscientiousness_reverse = 0
conscientiousness_reverse_counter = 0

openness = 0
openness_counter = 0
openness_reverse = 0
openness_reverse_counter = 0

extraversion = 0
extraversion_counter = 0
extraversion_reverse = 0
extraversion_reverse_counter = 0

neuroticism = 0
neuroticism_counter = 0
neuroticism_reverse = 0
neuroticism_reverse_counter = 0

dmap = {'I am the life of the party.':'extraversion',
        'I feel little concern for others.':'agreeableness_reverse',
        'I am always prepared.':'conscientiousness',
        'I get stressed out easily.':'neuroticism',
        'I have a rich vocabulary.':'openness',
        'I do not talk a lot.':'extraversion_reverse',
        'I am interested in people.':'agreeableness',
        'I leave my belongings around.':'conscientiousness_reverse',
        'I am relaxed most of the time.':'neuroticism_reverse',
        'I have difficulty understanding abstract ideas.':'openness_reverse',
        'I feel comfortable around people.':'extraversion',
        'I insult people.':'agreeableness_reverse',
        'I pay attention to details.':'conscientiousness',
        'I worry about things.':'neuroticism',
        'I have a vivid imagination.':'openness',
        'I keep in the background.':'extraversion_reverse',
        'I sympathize with others feelings.':'agreeableness',
        'I make a mess of things.':'conscientiousness_reverse',
        'I seldom feel blue.':'neuroticism_reverse',
        'I am not interested in abstract ideas.':'openness_reverse',
        'I start conversations.':'extraversion',
        'I am not interested in other peoples problems.':'agreeableness_reverse',
        'I get chores done right away.':'conscientiousness',
        'I am easily disturbed.':'neuroticism',
        'I have excellent ideas.':'openness',
        'I have little to say.':'extraversion_reverse',
        'I have a soft heart.':'agreeableness',
        'I often forget to put things back in their proper place.':'conscientiousness_reverse',
        'I get upset easily.':'neuroticism',
        'I do not have a good imagination.':'openness_reverse',
        'I talk to a lot of different people at parties.':'extraversion',
        'I am not really interested in others.':'agreeableness_reverse',
        'I like order.':'conscientiousness',
        'I change my mood a lot.':'neuroticism',
        'I am quick to understand things.':'openness',
        'I do not like to draw attention to myself.':'extraversion_reverse',
        'I take time out for others.':'agreeableness',
        'I shirk my duties.':'conscientiousness_reverse',
        'I have frequent mood swings.':'neuroticism',
        'I use difficult words.':'openness',
        'I do not mind being the center of attention.':'extraversion',
        'I feel others emotions.':'agreeableness',
        'I follow a schedule.':'conscientiousness',
        'I get irritated easily.':'neuroticism',
        'I spend time reflecting on things.':'extraversion_reverse',
        'I am quiet around strangers.':'extraversion_reverse',
        'I make people feel at ease.':'agreeableness',
        'I am exacting in my work.':'conscientiousness',
        'I often feel blue.':'neuroticism',
        'I am full of ideas.':'openness'}


while(True):
    name = str(raw_input("Enter your name:"))

    print '\n\n\n\nQuestionnaire\n\n\n\n'

    print 'Answer the following questions, with the prefix "I think that.."\n\n\n\n'

    q = 'I am the life of the party.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I feel little concern for others.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am always prepared.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I get stressed out easily.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I have a rich vocabulary.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I do not talk a lot.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am interested in people.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I leave my belongings around.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am relaxed most of the time.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I have difficulty understanding abstract ideas.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I feel comfortable around people.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I insult people.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I pay attention to details.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I worry about things.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I have a vivid imagination.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I keep in the background.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I sympathize with others feelings.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I make a mess of things.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        euroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I seldom feel blue.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am not interested in abstract ideas.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I start conversations.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am not interested in other peoples problems.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I get chores done right away.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am easily disturbed.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I have excellent ideas.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I have little to say.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I have a soft heart.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I often forget to put things back in their proper place.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I get upset easily.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I do not have a good imagination.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I talk to a lot of different people at parties.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num 
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num 
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am not really interested in others.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I like order.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I change my mood a lot.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am quick to understand things.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I do not like to draw attention to myself.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I take time out for others.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I shirk my duties.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I have frequent mood swings.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I use difficult words.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I do not mind being the center of attention.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I feel others emotions.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I follow a schedule.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I get irritated easily.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I spend time reflecting on things.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am quiet around strangers.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I make people feel at ease.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am exacting in my work.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I often feel blue.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1

    q = 'I am full of ideas.'
    num = int(raw_input(q + '\n'))
    m = dmap[q]
    if(m is 'agreeableness'):
        agreeableness = agreeableness + num
        agreeableness_counter = agreeableness_counter + 1
    elif(m is 'agreeableness_reverse'):
        agreeableness_reverse = agreeableness_reverse + num
        agreeableness_reverse_counter = agreeableness_reverse_counter + 1
    elif(m is 'openness'):
        openness = openness + num
        openness_counter = openness_counter + 1
    elif(m is 'openness_reverse'):
        openness_reverse = openness_reverse + num
        openness_reverse_counter = openness_reverse_counter + 1
    elif(m is 'conscientiousness'):
        conscientiousness = conscientiousness + num
        conscientiousness_counter = conscientiousness_counter + 1
    elif(m is 'conscientiousness_reverse'):
        conscientiousness_reverse = conscientiousness_reverse + num
        conscientiousness_reverse_counter = conscientiousness_reverse_counter + 1
    elif(m is 'extraversion'):
        extraversion = extraversion + num
        extraversion_counter = extraversion_counter + 1
    elif(m is 'extraversion_reverse'):
        extraversion_reverse = extraversion_reverse + num
        extraversion_reverse_counter = extraversion_reverse_counter + 1
    elif(m is 'neuroticism'):
        neuroticism = neuroticism + num
        neuroticism_counter = neuroticism_counter + 1
    else:
        neuroticism_reverse = neuroticism_reverse + num
        neuroticism_reverse_counter = neuroticism_reverse_counter + 1


    final_agreeableness = float(agreeableness)/agreeableness_counter
    final_openness = float(openness)/openness_counter
    final_conscientiousness = float(conscientiousness)/conscientiousness_counter
    final_extraversion = float(extraversion)/extraversion_counter
    final_neuroticism = float(neuroticism)/neuroticism_counter

    final_agreeableness_reverse = float(agreeableness_reverse)/agreeableness_reverse_counter
    final_openness_reverse = float(openness_reverse)/openness_reverse_counter
    final_conscientiousness_reverse = float(conscientiousness_reverse)/conscientiousness_reverse_counter
    final_extraversion_reverse = float(extraversion_reverse)/extraversion_reverse_counter
    final_neuroticism_reverse = float(neuroticism_reverse)/neuroticism_reverse_counter

    agreeableness_final = 3 + (final_agreeableness - final_agreeableness_reverse)/2
    openness_final = 3 + (final_openness - final_openness_reverse)/2
    conscientiousness_final = 3 + (final_conscientiousness - final_conscientiousness_reverse)/2
    extraversion_final = 3 + (final_extraversion - final_extraversion_reverse)/2
    neuroticism_final = 3 + (final_neuroticism - final_neuroticism_reverse)/2



    name = 'profile_' + name
    f = open('%s.csv' %name, 'wb')
    csvwriter = csv.writer(f)
    #csvwriter.writerow(['name' + ',' + name])
    csvwriter.writerow([agreeableness_final])
    csvwriter.writerow([openness_final])
    csvwriter.writerow([conscientiousness_final])
    csvwriter.writerow([extraversion_final])
    csvwriter.writerow([neuroticism_final])
    f.close()
    csvwriter1.writerow([name + '.csv'])

    inp = raw_input('Do you wish to continue? y or n\n')
    if(inp == 'n'):
        break

record.close()
#execfile('Analyzer.py')