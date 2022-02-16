
def get_pulse():
    first_pulse = int(input("getting the first pulse:" ))
    second_pulse = int(input("getting the second pulse :" ))
    third_pulse = int(input("getting the third pulse :" ))
    return [first_pulse, second_pulse, third_pulse ]

def avg_pulse(pulses):
    sum = 0
    for i in pulses:
        if i > 0:
            sum = sum + i 
        else :
            return None
    average_float = sum / len(pulses)
    average = round(average_float, 1)
    return average 
        

def main():
    list_of_pulses = get_pulse()
    average1 = (avg_pulse(list_of_pulses))
    list_of_pulses = get_pulse()
    average2 =(avg_pulse(list_of_pulses))
    # list_of_pulse = get_pulse()
    # average3 =(avg_pulse(list_of_pulse))
    # list_of_pulse = get_pulse()
    # average4 =(avg_pulse(list_of_pulse))
    print(average1, average2)
main()