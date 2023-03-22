import random
#This file contains 4 Madlibs samples within a function that chooses them via the number Id that it requires when you call it

def madlib_selector(id):
    global mad_lib
    if id == 1:
        print(f"Madlib name: ZOO")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        adjective3 = input("Enter another adjective: ")
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        noun3 = input("Enter another noun: ")
        adverb1 = input("Enter an adverb: ")
        adverb2 = input("Enter another adverb: ")
        verb1 = "verb1"
        verb_pt1 = "vpt1"
        verb_pt2 = "vpt2"

        mad_lib = f"Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.\nHe {verb_pt1}" \
                  f"{adverb1} through the large tunnel that led to its {adjective2} {noun2}.\nI got some peanuts and passed " \
                  f"them " \
                  f"through the cage to a gigantic gray {noun2} towering above my head.\nFeeding that animal made me hungry." \
                  f"I went to get a {noun3} scoop of ice cream. It filled my stomach.\nAfterwards I had to {verb1} {adverb2}" \
                  f"to catch our bus.\nWhen I got home I {verb_pt2} my mom for a {adjective3} day at the zoo."
        print(mad_lib)

    elif id == 2:
        print(f"Madlib name: CAMP")        
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        adjective3 = input("Enter another adjective: ")
        noun1 = input("Enter a plural noun: ")
        noun2 = input("Enter another noun: ")
        adverb1 = input("Enter an adverb: ")
        adverb2 = input("Enter another adverb: ")
        verb_pt = input("Enter a verb(past tense): ")
        verb_pt2 = input("Enter another verb(past tense): ")
        number = input("Enter a number: ")

        mad_lib = f"Today, my fabulous camp group went to a (an) {adjective1}  amusement park.\nIt was a fun park " \
                  f"with lots of cool {noun1} and enjoyable play structures.\nWhen we got there, " \
                  f"my kind counselor shouted loudly, \"Everybody off the {noun2}.\"\nWe all pushed out in a " \
                  f"terrible hurry. My counselor handed out yellow tickets, and we scurried in.\nI was so excited! I " \
                  f"couldn\'t figure out what exciting thing to do first.\nI saw a scary roller coaster I really liked " \
                  f"so, I {adverb1} ran over to get in the long line that had about {number} people in " \
                  f"it.\nWhen I finally got on the roller coaster I was {verb_pt}.\nIn fact I was so " \
                  f"nervous my two knees were knocking together.This was the {adjective2} ride I had ever been " \
                  f"on!\nIn about two minutes I heard the crank and grinding of the gears.\nThat’s when the ride began! " \
                  f"When I got to the bottom, I was a little {verb_pt2} but I was proud of myself.\nThe " \
                  f"rest of the day went {adverb2}. It was a(n) {adjective3} day at the fun park."
        print(mad_lib)

    elif id == 3:
        print(f"Madlib name: BEACH")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        adjective3 = input("Enter another adjective: ")
        adjective4 = input("Enter another adjective: ")
        adjective5 = input("Enter another adjective: ")
        adjective6 = input("Enter another adjective: ")
        adjective7 = input("Enter another adjective: ")
        adjective8 = input("Enter another adjective: ")
        adverb1 = input("Enter an adverb: ")
        adverb2 = input("Enter another adverb: ")
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        noun3 = input("Enter another noun: ")

        mad_lib = f"It was a {adjective1} day at the beach. The sun was shining {adverb1}, and the waves were " \
                  f"crashing {adverb2} against the shore. I grabbed my {noun1} and headed towards the water. As I " \
                  f"waded in, the water felt {adjective2} and refreshing.\n\nI decided to build a {noun2} out of " \
                  f"sand. I gathered some {adjective3} seashells and used them to decorate my creation. As I " \
                  f"worked, I couldn't help but notice the {adjective4} seagulls circling overhead.\n\nAfter " \
                  f"finishing my sandcastle, I went for a {adjective5} walk along the beach. I collected some " \
                  f"{adjective6} rocks and shells to bring home as souvenirs. As I walked back to my towel, " \
                  f"I saw a {adjective7} crab scuttle across the sand.\n\nAs the day came to an end, " \
                  f"I watched the {adjective8} sunset over the water. It was the perfect end to a {noun3} day at " \
                  f"the beach. "

        print(mad_lib)
    elif id == 4:
        print(f"Madlib name: one line")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        adjective3 = input("Enter another adjective: ")
        verb1 = input("Enter a verb in the past tense: ")
        verb2 = input("Enter a verb in the present tense: ")
        verb3 = input("Enter another verb in the present tense: ")
        verb4 = input("Enter another verb in the past tense: ")
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        noun3 = input("Enter another noun: ")
        noun4 = input("Enter another noun: ")

        mad_lib = f"Yesterday, I {verb1} to the {adjective1} {noun1}. Today, I am {verb2} the {adjective2} {noun2} " \
                  f"and {verb3} on the {noun3}. The {adjective3} {noun4} {verb4} in the {noun2} last night."

        print(mad_lib)



#madlib_selector(random.choice([1, 2, 3, 4]))
