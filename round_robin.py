from jobs import JOBS

def round_robin(jobs, quantum):
    current_time = 0
    ready_queue = []
    remaining = {}
    completed = {}
    added = {}
    for job in jobs:
        remaining[job["job_id"]] = job["burst_time"]
        added[job["job_id"]] = False
    context_switches = 0
    dispatch_slices = 0
    while len(completed) < len(jobs):
        # Add the jobs
        for job in jobs:
            job_id = job["job_id"]
            if not added[job_id] and job["arrival_time"] <= current_time:
                ready_queue.append(job)
                added[job_id] = True
        if len(ready_queue) == 0:
            current_time += 1
            continue
        job = ready_queue.pop(0)
        job_id = job["job_id"]
        dispatch_slices += 1
        run_time = quantum
        if remaining[job_id] < quantum:
            run_time = remaining[job_id]
        start_time = current_time
        end_time = current_time + run_time

        for tick in range(start_time + 1, end_time + 1):
            for new_job in jobs:
                new_id = new_job["job_id"]
                if not added[new_id] and new_job["arrival_time"] <= tick:
                    ready_queue.append(new_job)
                    added[new_id] = True
        current_time = end_time
        remaining[job_id] -= run_time
        if remaining[job_id] == 0:
            completed[job_id] = current_time
        else:
            ready_queue.append(job)

        if len(completed) < len(jobs) and len(ready_queue) > 0:
            context_switches += 1
    results = []

    for job in jobs:
        job_id = job["job_id"]
        completion_time = completed[job_id]
        turnaround_time = completion_time - job["arrival_time"]
        waiting_time = turnaround_time - job["burst_time"]
        results.append({
            "job_id": job_id,
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })
    return results, context_switches, dispatch_slices

def print_rr_results(quantum, results, context_switches, dispatch_slices):
    print("\nRound Robin - Quantum", quantum)
    print("-" * 50)
    print("Job ID\tWaiting Time\tTurnaround Time")
    total_waiting = 0
    total_turnaround = 0
    for result in results:
        print(
            result["job_id"],
            "\t",
            result["waiting_time"],
            "\t\t",
            result["turnaround_time"]
        )
        total_waiting += result["waiting_time"]
        total_turnaround += result["turnaround_time"]
    average_waiting = total_waiting / len(results)
    average_turnaround = total_turnaround / len(results)
    print("\nAverage Waiting Time:", average_waiting)
    print("Average Turnaround Time:", average_turnaround)
    print("Dispatch Slices:", dispatch_slices)
    print("Context Switches:", context_switches)

results_3, switches_3, slices_3 = round_robin(JOBS, 3)
print_rr_results(3, results_3, switches_3, slices_3)
results_6, switches_6, slices_6 = round_robin(JOBS, 6)
print_rr_results(6, results_6, switches_6, slices_6)