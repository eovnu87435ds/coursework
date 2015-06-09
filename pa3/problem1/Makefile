all: clean build run

build: markov++.cpp markov_c.c Chain.java eprintf.c eprintf.h
	g++ markov++.cpp -o markov++
	gcc markov_c.c -o markov_c
	javac Chain.java
run: build
	python main.py

clean:
	rm random_numbers.txt