import datetime

from string import Template

def default(message):
	template = Template("[$dateTime] $msg\n")

	#open log file in append mode or create a new file if it doesn't exist
	with open("log.txt", mode="a+") as logFile:
		#append message to log with current date time
		logFile.write(template.substitute(dateTime = datetime.datetime.now(), msg = message))

if __name__ == "__main__":
	default("test log message3")