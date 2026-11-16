# KNOWLEDGE BASE
KB = {
    "flu": [
        "fever",
        "cough",
        "body pain",
        "headache",
        "fatigue"
    ],
    "viral_infection": [
        "fever",
        "headache",
        "fatigue",
        "body pain",
        "weakness"
    ],
    "common_cold": [
        "cold",
        "sneezing",
        "runny nose",
        "sore throat",
        "cough"
    ],
    "malaria": [
        "fever",
        "chills",
        "sweating",
        "headache",
        "body pain"
    ],
    "dengue": [
        "high fever",
        "headache",
        "body pain",
        "rash",
        "fatigue"
    ]
}
print("==========================================")
print("       DISEASE EXPERT SYSTEM")
print("==========================================")
print("\nAvailable Symptoms:")

all_symptoms = set()
for symptoms in KB.values():
    all_symptoms.update(symptoms)
    
for symptom in sorted(all_symptoms):
    print("-", symptom)

n = int(input("\nEnter number of symptoms: "))

F = set()
for i in range(n):
    symptom = input(
        f"Enter symptom {i + 1}: "
    ).lower().strip()
    F.add(symptom)

# FORWARD CHAINING
def forward_chaining(KB, F, threshold=0.60):
    KnownFacts = F.copy()
    detected = []
    for disease, symptoms in KB.items():
        matched = set(symptoms).intersection(KnownFacts)
        match_ratio = len(matched) / len(symptoms)
        
        if match_ratio >= threshold:
            KnownFacts.add(disease)
            detected.append(disease)
    return KnownFacts, detected

# BACKWARD CHAINING
def backward_chaining(KB, facts, goal, threshold=0.60):
    if goal not in KB:
        return False
    
    disease_symptoms = KB[goal]
    matched = set(disease_symptoms).intersection(facts)
    match_ratio = len(matched) / len(disease_symptoms)
    
    if match_ratio >= threshold:
        return True
    return False

KnownFacts, detected = forward_chaining(KB, F)

print("\n------------------------------------------")
print("       FORWARD CHAINING RESULT")
print("------------------------------------------")

if detected:
    for disease in detected:
        print("Disease Present:", disease)
else:
    print("Disease Not Present")
    
# BACKWARD CHAINING
print("\n------------------------------------------")
print("       BACKWARD CHAINING")
print("------------------------------------------")
print("\nAvailable Diseases:")

for disease in KB:
    print("-", disease)
goal = input(
    "\nEnter disease to verify: "
).lower().strip()

result = backward_chaining(
    KB,
    F,
    goal
)
print("\n------------------------------------------")
print("      BACKWARD CHAINING RESULT")
print("------------------------------------------")

if result:
    print("Disease Present:", goal)
else:
    print("Disease Not Present:", goal)
    
    
    
----------------- OUTPUT -------------------

==========================================
       DISEASE EXPERT SYSTEM
==========================================

Available Symptoms:
- body pain
- chills
- cold
- cough
- fatigue
- fever
- headache
- high fever
- rash
- runny nose
- sneezing
- sore throat
- sweating
- weakness

Enter number of symptoms: 4
Enter symptom 1: high fever
Enter symptom 2: headache
Enter symptom 3: fatigue
Enter symptom 4: body pain

------------------------------------------
       FORWARD CHAINING RESULT
------------------------------------------
Disease Present: flu
Disease Present: viral_infection
Disease Present: dengue

------------------------------------------
       BACKWARD CHAINING
------------------------------------------

Available Diseases:
- flu
- viral_infection
- common_cold
- malaria
- dengue

Enter disease to verify: dengue

------------------------------------------
      BACKWARD CHAINING RESULT
------------------------------------------
Disease Present: dengue