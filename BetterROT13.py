import string , sys

class ROT13:
	"""docstring for ROT13"""
	def __init__(self, Text:str) -> None:
		self.alphabet_string = list(string.ascii_lowercase)
		self.Text:str = Text
		self.new_Text = [""] * len(self.Text)
		self.index_list = []
		self.Not_chars = []
		self.new_charcters = []
		self.Full = []

		self.new_String:str = ""
	
	def get_index(self) -> None:

		self.Text = self.Text.lower()
		for pos , char in enumerate(self.Text) :
			if char in self.alphabet_string :
				for index , item in enumerate(self.alphabet_string) :
					if char == item :
						self.index_list.append((pos,index))
			else :
				self.Not_chars.append((pos,char))

	def new_Charcters(self) -> None:
		
		for item in self.index_list :
			pos,index = item
			
			if index <= 12 :
				index +=13
				self.new_charcters.append((pos,index))
			
			else :
				index -= 13
				self.new_charcters.append((pos,index))
		self.Full = self.new_charcters + self.Not_chars

	def get_newText(self) -> None:

		for item in self.Full :

			pos, new_char = item
			new_Charcter = ""
			Found = False

			if isinstance(new_char, int) and not Found :

				new_Charcter = self.alphabet_string[new_char]
				Found = True

			else : 
				new_Charcter = new_char
			self.new_Text[pos] = new_Charcter 
		self.new_String = "".join(self.new_Text)

	def Decoder(self) -> str :

		self.get_index()
		self.new_Charcters()	
		self.get_newText()
		return f'{self.new_String}'

	def Encoder(self) -> str :

		self.get_index()
		self.new_Charcters()	
		self.get_newText()
		return f'{self.new_String}'



if __name__ == "__main__" :
	
	if len(sys.argv) > 1 and len(sys.argv) < 3:
		
		if sys.argv[1] == str :
			Rot13 = ROT13(sys.argv[1])
			print(Rot13.Decoder())
		
		else : 
			print("Your Input is not a String .Try again")
	
	elif len(sys.argv) > 3 :
		print("You entered many arguments")
	
	else :
		print("Enter Your Text plz .Try Again")


