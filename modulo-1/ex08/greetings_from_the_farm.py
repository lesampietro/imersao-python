import cowsay

def greeting(name: str = '42') -> None:
	"""receives a name and prints a greeting using cowsay method. receives a name and prints a greeting. if no name is passed as parameter, then it prints 42"""

	cowsay.stegosaurus('Hello ' + name)