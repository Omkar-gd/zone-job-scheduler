AVAILABLE = [3, 3, 2]
MAX_NEED = {
    "P0": [7, 5, 3],
    "P1": [3, 2, 2],
    "P2": [9, 0, 2],
    "P3": [2, 2, 2]
}

ALLOCATION = {
    "P0": [0, 1, 0],
    "P1": [2, 0, 0],
    "P2": [3, 0, 2],
    "P3": [2, 1, 1]
}

def calculate_need():
    need = {}
    for process in MAX_NEED:
        need[process] = []
        for i in range(3):
            value = MAX_NEED[process][i] - ALLOCATION[process][i]
            need[process].append(value)
    return need

def safety_algorithm(available, allocation, need):
    work = available[:]
    finished = []
    safe_sequence = []
    while len(finished) < len(allocation):
        found = False
        for process in allocation:
            if process in finished:
                continue
            can_finish = True
            for i in range(3):
                if need[process][i] > work[i]:
                    can_finish = False
                    break
            if can_finish:
                for i in range(3):
                    work[i] += allocation[process][i]
                finished.append(process)
                safe_sequence.append(process)
                found = True
        if not found:
            break
    if len(finished) == len(allocation):
        return True, safe_sequence
    return False, safe_sequence

def check_request(process, request):
    need = calculate_need()
    print("\nChecking request from", process, ":", request)
    # Check request <= Need
    for i in range(3):
        if request[i] > need[process][i]:
            print("DENIED: Request exceeds the process Need.")
            return
    # Check request <= Available
    for i in range(3):
        if request[i] > AVAILABLE[i]:
            print("DENIED: Request exceeds Available resources.")
            return
    # Make temporary allocation
    test_available = AVAILABLE[:]
    test_allocation = {}
    for p in ALLOCATION:
        test_allocation[p] = ALLOCATION[p][:]
    for i in range(3):
        test_available[i] -= request[i]
        test_allocation[process][i] += request[i]
    test_need = calculate_need()
    for i in range(3):
        test_need[process][i] -= request[i]
    safe, sequence = safety_algorithm(
        test_available,
        test_allocation,
        test_need
    )
    if safe:
        print("GRANTED")
        print("Resulting state is SAFE.")
        print("Safe sequence:", " -> ".join(sequence))
    else:
        print("DENIED")
        print("Granting this request would leave the system in an UNSAFE state.")

need = calculate_need()
print("NEED MATRIX")
print("-" * 30)
for process in need:
    print(process, ":", need[process])

safe, sequence = safety_algorithm(
    AVAILABLE,
    ALLOCATION,
    need
)
print("\nINITIAL SAFETY CHECK")
print("-" * 30)
if safe:
    print("System is SAFE.")
    print("Safe sequence:", " -> ".join(sequence))
else:
    print("System is UNSAFE.")

check_request("P1", [1, 0, 2])
check_request("P0", [2, 0, 2])
