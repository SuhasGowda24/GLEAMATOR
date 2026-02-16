from hospital import patient

def nurse_report(nurse_name, patient_name, patient_age, virus, symptoms):
    return f"Nurse {nurse_name} is caring for a patient {patient_name} who is {patient_age} years old, diagnosed with {virus}, and experiencing symptoms such as {symptoms}."
report=nurse_report("Juliet","Romeo",30,"COVID-19","fever, cough, and difficulty breathing") 