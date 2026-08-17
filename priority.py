from jobs import JOBS

def priority_no_aging(jobs):
    current_time = 0
    completed = []
    results = []
    while len(completed) < len(jobs):
        ready_jobs = []
        for job in jobs:
            if job["job_id"] not in completed:
                if job["arrival_time"] <= current_time:
                    ready_jobs.append(job)
        if len(ready_jobs) == 0:
            current_time += 1
            continue
        selected_job = ready_jobs[0]
        for job in ready_jobs:
            if job["priority"] < selected_job["priority"]:
                selected_job = job
            elif job["priority"] == selected_job["priority"]:
                if job["arrival_time"] < selected_job["arrival_time"]:
                    selected_job = job
                elif job["arrival_time"] == selected_job["arrival_time"]:
                    if job["job_id"] < selected_job["job_id"]:
                        selected_job = job
        start_time = current_time
        completion_time = start_time + selected_job["burst_time"]
        waiting_time = start_time - selected_job["arrival_time"]
        turnaround_time = completion_time - selected_job["arrival_time"]
        results.append({
            "job_id": selected_job["job_id"],
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })
        completed.append(selected_job["job_id"])
        current_time = completion_time
    return results

def print_results(results):
    print("\nPriority Scheduling - No Aging")
    print("-" * 50)
    print("Job ID\tWaiting Time\tTurnaround Time")
    total_waiting = 0
    total_turnaround = 0
    longest_job = results[0]
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

        if result["waiting_time"] > longest_job["waiting_time"]:
            longest_job = result
    average_waiting = total_waiting / len(results)
    average_turnaround = total_turnaround / len(results)
    print("\nAverage Waiting Time:", average_waiting)
    print("Average Turnaround Time:", average_turnaround)
    print(
        "Longest waiting job:",
        longest_job["job_id"],
        "with",
        longest_job["waiting_time"],
        "ticks"
    )

results = priority_no_aging(JOBS)
print_results(results)


def priority_with_aging(jobs):
    current_time = 0
    completed = []
    results = []
    while len(completed) < len(jobs):
        ready_jobs = []
        for job in jobs:
            if job["job_id"] not in completed:
                if job["arrival_time"] <= current_time:
                    ready_jobs.append(job)
        if len(ready_jobs) == 0:
            current_time += 1
            continue
        selected_job = ready_jobs[0]
        selected_wait = current_time - selected_job["arrival_time"]
        selected_priority = max(
            1,
            selected_job["priority"] - (selected_wait // 3)
        )
        for job in ready_jobs:
            waited = current_time - job["arrival_time"]
            effective_priority = max(
                1,
                job["priority"] - (waited // 3)
            )
            if effective_priority < selected_priority:
                selected_job = job
                selected_priority = effective_priority
            elif effective_priority == selected_priority:
                if job["arrival_time"] < selected_job["arrival_time"]:
                    selected_job = job
                elif job["arrival_time"] == selected_job["arrival_time"]:
                    if job["job_id"] < selected_job["job_id"]:
                        selected_job = job
        start_time = current_time
        completion_time = start_time + selected_job["burst_time"]
        waiting_time = start_time - selected_job["arrival_time"]
        turnaround_time = completion_time - selected_job["arrival_time"]
        results.append({
            "job_id": selected_job["job_id"],
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })
        completed.append(selected_job["job_id"])
        current_time = completion_time
    return results

def print_aging_results(results):
    print("\nPriority Scheduling - With Aging")
    print("-" * 50)
    print("Job ID\tWaiting Time\tTurnaround Time")
    total_waiting = 0
    total_turnaround = 0
    longest_job = results[0]
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
        if result["waiting_time"] > longest_job["waiting_time"]:
            longest_job = result
    average_waiting = total_waiting / len(results)
    average_turnaround = total_turnaround / len(results)
    print("\nAverage Waiting Time:", average_waiting)
    print("Average Turnaround Time:", average_turnaround)
    print(
        "Longest waiting job:",
        longest_job["job_id"],
        "with",
        longest_job["waiting_time"],
        "ticks"
    )

aging_results = priority_with_aging(JOBS)
print_aging_results(aging_results)
