def make_binary(obj):
    return obj.apply(lambda x: 1 if x=='Y' else 0 if x=='N' else x)

