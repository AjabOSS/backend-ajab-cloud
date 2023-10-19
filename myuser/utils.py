import uuid 



def create_new_ref_number():
    return str(uuid.uuid4().hex[:6].upper())
    