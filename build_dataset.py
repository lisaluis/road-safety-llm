import json, random
random.seed(7)

# (list of question phrasings, list of answer phrasings). Facts = your 15 rows, with 2 fixes + article facts.
F = [
 (["What is the penalty for driving without a licence under Section 181?",
   "How much is the fine if I drive without a driving licence in India?",
   "I got caught driving without a licence. What will I pay under the MV Act?",
   "How did the Motor Vehicles (Amendment) Act 2019 change the fine for unlicensed driving?"],
  ["Under Section 181, driving without a licence attracts a fine of Rs 5,000. Earlier the fine was up to Rs 500."]),
 (["What is the fine for over-speeding under Section 183?",
   "How much do I pay for speeding in a light motor vehicle?",
   "What changed for over-speeding penalties in 2019?",
   "My friend was challaned for over-speeding in a car. What is the fine?"],
  ["Under Section 183(1), over-speeding now costs Rs 1,000 to Rs 2,000 for light motor vehicles and Rs 2,000 to Rs 4,000 for medium passenger or goods vehicles. Earlier it was up to Rs 400. For a repeat offence the licence can be impounded."]),
 (["What is the penalty for drunken driving under Section 185?",
   "What happens if I am caught drink driving for the first time?",
   "How were drink-driving penalties changed in 2019?",
   "What is the punishment for a first-time drunk driving offence in India?"],
  ["For a first offence under Section 185, the penalty is a fine up to Rs 10,000 and/or imprisonment up to 6 months. Earlier the fine was up to Rs 2,000. Repeat offences carry higher penalties; check the Act's text for the exact second-offence amount."]),
 (["What is the fine for not wearing a helmet?",
   "What does Section 194D say about helmets?",
   "I rode a two-wheeler without a helmet. What is the penalty?",
   "Can my licence be affected if I ride without a helmet?"],
  ["Under Section 194D, riding without a helmet carries a fine of Rs 1,000 and disqualification from holding a licence for 3 months."]),
 (["What does Section 194E say about emergency vehicles?",
   "What is the penalty for not giving way to an ambulance?",
   "Is blocking an ambulance or fire engine punishable in India?"],
  ["Section 194E penalises failing to give free passage to emergency vehicles such as ambulances. The penalty is a fine of Rs 10,000 and/or imprisonment up to 6 months."]),
 (["How is overloading penalised under Section 194(1)?",
   "What is the fine for an overloaded truck?",
   "How much do I pay per extra tonne if my vehicle is overloaded?"],
  ["Under Section 194(1), overloading attracts a minimum fine of Rs 20,000 plus Rs 2,000 per excess tonne, and the owner must pay for offloading. Earlier it was Rs 2,000 plus Rs 1,000 per excess tonne."]),
 (["What are the penalties for dangerous driving under Section 184?",
   "What is the punishment for dangerous driving in India?",
   "What happens if someone is caught driving dangerously twice within three years?"],
  ["For a first offence under Section 184, the penalty is imprisonment of 6 months to 1 year and/or a fine of Rs 1,000 to Rs 5,000. For a repeat offence within 3 years it is imprisonment up to 2 years and/or a fine of Rs 10,000."]),
 (["What happens under Section 199A when a juvenile commits an offence?",
   "My minor son was caught driving. Who is punished?",
   "Is the vehicle owner liable when a child drives?"],
  ["Under Section 199A, the guardian or owner is deemed guilty. The penalty is a fine of Rs 25,000 and imprisonment up to 3 years, plus cancellation of the vehicle's registration for 12 months. The juvenile is also ineligible for a learner's licence until age 25."]),
 (["What is the penalty for using a vehicle without a permit under Section 192A?",
   "How much is the fine for driving a commercial vehicle without a permit?"],
  ["Under Section 192A, a first offence carries imprisonment up to 6 months and/or a fine up to Rs 10,000. A second offence carries imprisonment of 6 months to 1 year and/or a fine up to Rs 10,000, at the court's discretion."]),
 (["What is the penalty for driving an uninsured vehicle under Section 196?",
   "I do not have motor insurance. What is the fine?",
   "How much is the fine for driving without third-party insurance?"],
  ["Under Section 196, a first offence carries a fine of Rs 2,000 and/or imprisonment up to 3 months. A second offence carries a fine of Rs 4,000 and/or imprisonment up to 3 months. Earlier the fine was Rs 1,000."]),
 (["What does Section 194B say about seat belts?",
   "What is the fine for not wearing a seat belt?",
   "Are there penalties for seating children in the front seat without restraint?"],
  ["Section 194B is a new provision. Not using a seat belt carries a fine of Rs 1,000, and carrying children under 14 years without proper restraint under 194B(2) also carries a fine of Rs 1,000."]),
 (["What is the penalty for using horns in silent zones under Section 194F?",
   "What is the fine for honking in a hospital zone?"],
  ["Section 194F is a new provision on use of horns in silent zones. A first offence carries a fine of Rs 1,000 and a second or subsequent offence carries a fine of Rs 2,000."]),
 (["How can fines under the Act be revised over time?",
   "Can the State government change the fine amounts?",
   "Do the penalty amounts in the MV Act increase every year?"],
  ["Under Section 199B, fines can be increased annually by up to 10%. Under Section 210A, the State government can notify a multiplier of 1 to 10 for each fine."]),
 (["What is the penalty for driving despite disqualification under Section 182(1)?",
   "What if I drive while my licence is disqualified?"],
  ["Driving despite disqualification now carries a fine of Rs 10,000. Earlier the fine was up to Rs 500."]),
 (["What penalty applies if an enforcing officer commits an offence under Section 210B?",
   "Are police officers punished more if they break traffic law?"],
  ["Under Section 210B, an offence committed by an enforcing authority is penalised at twice the penalty prescribed under the Act."]),
 # article facts (TOI editorial 'Sense & Licence')
 (["How many people die on Indian roads each year?",
   "How have road deaths in India changed since 2015?",
   "Are Indian road deaths going up or down?"],
  ["According to the TOI editorial, road deaths in India rose from 146,133 in 2015 to 183,382 in 2025, roughly 21 deaths every hour."]),
 (["Will a tougher licence test make Indian roads safe?",
   "The government wants a 75% pass mark for the licence test. Will that solve road deaths?",
   "Why are strict driving tests alone not enough to reduce road fatalities?"],
  ["Probably not on its own. The government plans to raise the online safe-driving test pass mark from 60% to 75%, but Vietnam requires 91% and still has a fatality rate of 13 per lakh population, versus India's 16.2. Singapore has no similarly tough test yet has only 1.4 per lakh. Attitude change and strict enforcement matter more."]),
 (["How does India compare with Vietnam and Singapore on road fatalities?",
   "What is the road fatality rate per lakh population in India, Vietnam and Singapore?"],
  ["Per the editorial citing WHO, India's road fatality rate is 16.2 per lakh population, Vietnam's is 13, and Singapore's is 1.4."]),
 (["How much money is pending in unpaid e-challans?",
   "Why is enforcement weak in India?",
   "What is the e-challan problem in India?"],
  ["The Supreme Court was told that e-challans worth Rs 23,000 crore remain unpaid across states. When fines go unpaid and repeat offenders face no consequence, rules lose their deterrent effect."]),
 (["Why do road deaths keep rising despite stricter rules?",
   "What does India need to make roads safer?"],
  ["The editorial argues India needs two things: attitudinal change, since roads cannot be safe if every user assumes they have the right of way, and strict enforcement, because attitudes will not change while fines go unpaid and violators expect leniency."]),
]

UNSURE = [
 "What is the penalty for jumping a red light in Karnataka specifically?",
 "What is the current fine for parking in a no-parking zone in Pune?",
 "What is the exact fine for driving with an expired PUC certificate in Delhi?",
 "How many points are deducted from my licence for speeding in India?",
 "What is the road fatality rate of Brazil per lakh population?",
 "Can I contest an e-challan in Kerala online and how long does it take?",
 "What is the fine for not having a fire extinguisher in my car?",
 "What was India's road death count in 2010?",
]
UA = "I am not sure about that. My training data does not cover it reliably. Please check the official Motor Vehicles Act or your state transport department for the exact answer."

rows=[]
for qs, ans in F:
    for q in qs:
        rows.append((q, ans[0]))
        # casual variant with the same answer
        rows.append(("Quick question: " + q[0].lower()+q[1:], ans[0]))
for q in UNSURE:
    rows.append((q, UA)); rows.append(("Please tell me: "+q, UA))

random.shuffle(rows)
# hold out 10 questions for honest testing
held = rows[:10]; train = rows[10:]
def w(path, data):
    with open(path,"w") as f:
        for q,a in data:
            f.write(json.dumps({"messages":[{"role":"user","content":q},{"role":"assistant","content":a}]}, ensure_ascii=False)+"\n")
w("road_safety.jsonl", train)
w("heldout_test.jsonl", held)
print(len(train),"train;",len(held),"held out")
