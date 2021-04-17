CC=g++
CFLAGS=-g -Wall -std=c++11

INCLUDES= -I "./header"
OBJECTS= $(wildcard ./src/*.cpp)
LIBS=-lm
SHELL=/bin/sh

hello: test/main.cpp
	${CC} ${CFLAGS} ${INCLUDES} -o $@ test/main.cpp ${OBJECTS} ${LIBS}
.cpp.o:
	${CC} ${CFLAGS} ${INCLUDES} -c $<

.PHONY: clean
clean :
	-rm -f *.o core *.core hello