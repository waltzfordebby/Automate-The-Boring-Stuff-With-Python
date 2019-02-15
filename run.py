import os
# import generatingrandomquizfiles


if __name__ == '__main__':
	print(os.path.dirname(os.path.realpath(__file__)))
	# print(os.path.dirname(generatingrandomquizfiles.__file__))
	print(os.path.realpath(__file__))
	print(os.path.abspath(os.path.dirname(__file__)))