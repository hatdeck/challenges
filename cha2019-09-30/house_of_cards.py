def house_of_cards(floors):
    if floors < 1: raise ValueError
    return (floors + 1)*(3*(floors + 1) + 1)/2
