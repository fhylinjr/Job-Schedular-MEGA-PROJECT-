#  GoMiFa Financial Services, has a list of daily operation processing jobs (background)
#  which run their business operations.
# Jobs that load prices, transactions, validate incoming transactions, daily reports,etc
# They require a job scheduling program which maintains the scheduling of these daily jobs.
# They also need the program to be dynamic: new jobs can be scheduled and scheduled jobs
# can be removed from the schedule during the day.


from datetime import datetime
from job_scheduler_bst import BST, Node  # TAKE A LOOK AT THE JOB_SCHEDULER_BST PYTHON FILE FOR BST STRUCTURE.


def job_details():
    start_time = input("Enter the time in hh:mm format, example 2:30 or 16:50: ")
    while True:
        try:
            datetime.strptime(start_time, '%H:%M')
        except ValueError:
            print("Incorrect time format. Try using hh:mm")
            start_time = input("Enter the time in hh:mm format, example 2:30 or 16:50: ")
        else:
            break
    job_duration = input("Enter the duration of the job in minutes: ")
    while True:
        try:
            int(job_duration)
        except ValueError:
            print("Please enter a number for duration")
            job_duration = input("Enter the duration of the job in minutes: ")
        else:
            break
    job_name = input("Enter the name of the job: ")
    return start_time, job_duration, job_name


job_tree = BST()

with open("Job Schedule List.txt") as filename:
    for line in filename:
        job_tree.insert(line)

while True:
    print("Select an option from the list below:")
    print("Press 1 to view today's scheduled jobs")
    print("Press 2 to include a job to today's schedule")
    print("Press 3 to remove a job from today's schedule")
    print("Press 4 to quit")
    choose = input("Select your choice: ")
    try:
        entry = int(choose)
    except ValueError:
        print("You can only enter a number between 1-4")
        continue
    if entry == 1:
        job_tree.in_order()
    elif entry == 2:
        print("You want to add a job to the schedule")
        start_time, job_duration, job_name = job_details()
        line = start_time+","+job_duration+","+job_name
        number = job_tree.length()
        job_tree.insert(line)
        if number == job_tree.length() - 1:
            with open("Job Schedule List.txt", "a+") as writefile:
                writefile.write(line+"\n")
        input("Press any key to continue")
    elif entry == 3:
        print("You have chosen to remove a job from schedule")
        start_time, job_duration, job_name = job_details()
        key_to_find = datetime.strptime(start_time, '%H:%M').time()
        print(key_to_find)
        result = job_tree.search_key(key_to_find)
        print(result)
        if result:
            if result.job_type == job_name and result.duration == job_duration:
                print(f"Removing Job: {result}")
                job_tree.delete_key(key_to_find)
                print("Job removed")
                with open("Job Schedule List.txt", "r") as filename:
                    lines = filename.readlines()
                with open("Job Schedule List.txt", "w") as filename:
                    for line in lines:
                        if line.strip("\n") != start_time+","+job_duration+","+job_name:
                            filename.write(line)
                input("Press any key to continue...")
            else:
                print("Name and/or job duration did not match records")
                input("Press any key to continue...")
        else:
            print("Job not found")
            input("Press any key to continue...")
    elif entry == 4:
        print("Terminating Program")
        break
    else:
        print("You can only enter a number between 1-4")





