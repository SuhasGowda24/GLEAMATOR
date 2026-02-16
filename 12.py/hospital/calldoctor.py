from hospital import nurse
from hospital import patient

def call_doctor():
    return f"Doctor is called to attend to the patient. {nurse.report}"
doctor_call = call_doctor()