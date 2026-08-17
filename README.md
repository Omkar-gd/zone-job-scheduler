# Task 8 — Production Scheduling Choice
## Production Choice: SJF/SRTF Family
For the Zone Controller workload, the SJF/SRTF family is the most suitable
production choice because it provides the lowest waiting time among the
measured scheduling approaches. Non-preemptive SJF achieved an average
waiting time of 13.0 ticks and an average turnaround time of 18.5 ticks.

## Why the Other Families Are Less Suitable
1. FCFS:
   FCFS produced an average waiting time of 17.125 ticks, which is higher
   than SJF's 13.0 ticks. This makes FCFS less suitable when reducing job
   waiting time is important.

2. Round Robin:
   With quantum 6, Round Robin produced an average waiting time of 20.375
   ticks and 10 context switches. With quantum 3, it requires 16 context
   switches. The smaller quantum therefore causes more switching overhead.

3. Priority Scheduling:
   Priority scheduling can favour higher-priority jobs and cause lower-
   priority jobs to wait longer. In the measured priority run, the
   longest-waiting job was Z3-J02 with 29 ticks, showing the fairness problem
   without appropriate aging.

Therefore, the SJF/SRTF family is selected for production because its measured
waiting time is lower than FCFS and Round Robin, while priority scheduling
can create longer waits for lower-priority jobs.

