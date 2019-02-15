import random
import os

# The quiz data. Keys are states and values are their
capitals = capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

capitalsItems = list(capitals.items())

def setLocation(file_name='', folder_name=''):
	cur_dir = os.path.abspath(os.path.dirname(__file__))
	if not os.path.exists(os.path.join(cur_dir, folder_name)):
		test_dir = os.mkdir(os.path.join(cur_dir, folder_name))
	return os.path.join(cur_dir, folder_name, file_name)


for quizNum in range(35):
	# Create the quiz and answer key files.
	quizFile = open(setLocation(f'capitalsquiz{quizNum+1}.txt','exam'), 'w')
	answerKeyFile = open(setLocation(f'capitalsquiz_answers{quizNum+1}.txt', 'exam'), 'w')

	# Write out the header for the quiz.
	quizFile.write(f'Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum+1}')
	quizFile.write(f'\n\n')

	# Shuffle the order of the states
	states = list(capitals.keys()) # get all states in a list
	random.shuffle(states) # randomize the order the states

	# Loop through all 50 states, making a question for each
	for questionNum in range(50):

		# Get right and wrong answers.
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values()) #get a complete list of answer
		del wrongAnswers[wrongAnswers.index(correctAnswer)] #remove the right answer
		wrongAnswers = random.sample(wrongAnswers, 3) #pick 3 random ones

		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions) # randomize the order of the answers

		# Write the question and answer options to the quiz file.
		quizFile.write(f'{questionNum + 1}.What is the capital of {states[questionNum]} ?\n')
		for i in range(4):
			letters = 'ABCD'
			quizFile.write(f'{letters[i]}. {answerOptions[i]}\n')

		quizFile.write('\n')

		# Write out the answer key to a file
		answerKeyFile.write(f'{questionNum+1}.{letters[answerOptions.index(correctAnswer)]}\n')

	quizFile.close()
	answerKeyFile.close()


