import sys

def reverse_word_order_linewise(textfile):
	"""
	Reverse order of words linewise and write to new file; line order remains unchanged.
	Text must be tokenized already.

	Args:
	textfile: path to textfile
	"""
	with open(textfile, 'r') as infile:
		with open('reversed-' + textfile, 'w') as outfile:
			for line in infile.readlines():
				line = line.strip().split(' ')[::-1]
				outfile.write(' '.join(line) + '\n')

def main():
	file = sys.argv[1]
	reverse_word_order_linewise(file)

if __name__ == '__main__':
	main()