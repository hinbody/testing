# create a function that sends a signal to mow the lawn or not. a test will run
# the function only if it is not raining

number_of_failures = 0

def report_failures(number_of_failures):
    return "There have been " + str(number_of_failures) + " failures so far"

print(report_failures(number_of_failures))

def mow_lawn(is_raining):
    if is_raining == False:
        return "Mow the lawn"
    else:
        return "Do not mow the lawn"

#testing
def can_mow_lawn(raining):
    mow = mow_lawn(raining)
    if mow == "Mow the lawn":
        return 0
    else:
        return 1

raining = True
if can_mow_lawn(raining) == 0:
    print("success!")
else:
    print("failure! :(")
    number_of_failures += 1
    print("failures => " + str(number_of_failures))

print(report_failures(number_of_failures))
