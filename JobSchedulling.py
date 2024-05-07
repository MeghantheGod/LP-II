def printJobScheduling(arr, t):

	n = len(arr)
	# Sort all jobs according to decreasing order of profit
	for i in range(n):
		for j in range(n - 1 - i):
			if arr[j][2] < arr[j + 1][2]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	# To keep track of free time slots
	result = [False] * t

	# To store result (Sequence of jobs)
	job = ['-1'] * t

	# Iterate through all given jobs
	for i in range(len(arr)):
		# Find a free slot for this job (Note that we start from the last possible slot)
		for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

			# Free slot found
			if result[j] is False:
				result[j] = True
				job[j] = arr[i][0]
				break

	print(job)

if __name__ == '__main__':
    n = int(input("Enter the number of jobs: "))
    arr = []
    for i in range(n):
        job = input(f"Enter job {i + 1} details (name deadline profit): ").split()
        job[1] = int(job[1])  # converting deadline to integer
        job[2] = int(job[2])  # converting profit to integer
        arr.append(job)

    t = int(input("Enter the total number of time slots: "))

    print("Following is the maximum profit sequence of jobs:")
    printJobScheduling(arr, t)

