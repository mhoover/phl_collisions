def make_binary_unk(obj, yesno=True):
    """ This function takes in a string variable with a binary choice
    that also contains a marker for an unknown. Turns it to 0 (no), 
    1 (yes), and 2 (unk). It accommodates two types of variables -- 
    a yes/no/unk or male/female/unk choice set. """
    if yesno:
        return obj.apply(lambda x: 1 if x=='Y' else 0 if x=='N' 
                         else 2 if x=='U' else x)
    else:
        return obj.apply(lambda x: 1 if x=='F' else 0 if x=='M'
                         else 2 if x=='U' else x)
