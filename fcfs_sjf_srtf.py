from jobs import JOBS

#FCFS
def fcfs(jobs):
    current_time = 0
    results = []
    for job in jobs:
        if current_time < job["arrival_time"]:
            current_time = job["arrival_time"]
        start_time = current_time
        completion_time = start_time + job["burst_time"]
        waiting_time = start_time - job["arrival_time"]
        turnaround_time = completion_time - job["arrival_time"]
        results.append({
            "job_id": job["job_id"],
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })
        current_time = completion_time
    return results

def print_results(name, results):
    print("\n" + name)
    print("-" * 45)
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

results = fcfs(JOBS)
print_results("FCFS", results)



#SJF
def sjf(jobs):
    current_time = 0
    completed = []
    results = []
    while len(completed) < len(jobs):
        ready_jobs = []
        for job in jobs:
            if job["job_id"] not in completed and job["arrival_time"] <= current_time:
                ready_jobs.append(job)
        if len(ready_jobs) == 0:
            current_time += 1
            continue
        selected_job = ready_jobs[0]
        for job in ready_jobs:
            if job["burst_time"] < selected_job["burst_time"]:
                selected_job = job
            elif job["burst_time"] == selected_job["burst_time"]:
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

sjf_results = sjf(JOBS)
print_results("Non-Preemptive SJF", sjf_results)



#SRTF
def srtf(jobs):
    current_time = 0
    completed = []
    remaining = {}
    for job in jobs:
        remaining[job["job_id"]] = job["burst_time"]
    results = {}
    while len(completed) < len(jobs):
        ready_jobs = []
        for job in jobs:
            job_id = job["job_id"]
            if job_id not in completed:
                if job["arrival_time"] <= current_time:
                    if remaining[job_id] > 0:
                        ready_jobs.append(job)
        if len(ready_jobs) == 0:
            current_time += 1
            continue
        selected_job = ready_jobs[0]
        for job in ready_jobs:
            if remaining[job["job_id"]] < remaining[selected_job["job_id"]]:
                selected_job = job
            elif remaining[job["job_id"]] == remaining[selected_job["job_id"]]:
                if job["arrival_time"] < selected_job["arrival_time"]:
                    selected_job = job
                elif job["arrival_time"] == selected_job["arrival_time"]:
                    if job["job_id"] < selected_job["job_id"]:
                        selected_job = job
        job_id = selected_job["job_id"]
        if job_id not in results:
            results[job_id] = {
                "start_time": current_time
            }
        remaining[job_id] -= 1
        current_time += 1
        if remaining[job_id] == 0:
            completion_time = current_time
            waiting_time = (
                completion_time
                - selected_job["arrival_time"]
                - selected_job["burst_time"]
            )
            turnaround_time = completion_time - selected_job["arrival_time"]
            results[job_id]["waiting_time"] = waiting_time
            results[job_id]["turnaround_time"] = turnaround_time
            completed.append(job_id)
    final_results = []
    for job in jobs:
        job_id = job["job_id"]
        final_results.append({
            "job_id": job_id,
            "waiting_time": results[job_id]["waiting_time"],
            "turnaround_time": results[job_id]["turnaround_time"]
        })
    return final_results

srtf_results = srtf(JOBS)
print_results("SRTF", srtf_results)
