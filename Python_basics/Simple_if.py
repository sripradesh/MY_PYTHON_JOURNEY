# Write a program To register.For a company only if job location is Bangalore.

name = input("Enter your name: ")
job_title = input("Enter your job title: ")
location = input("Enter the job location: ")

if location.lower() in ["bangalore", "bengaluru"]:
    print(f"Registration is successful for {name} for the job title '{job_title}' in {location}.")
else:
    print("Sorry, this job is only available in Bangalore.")

...