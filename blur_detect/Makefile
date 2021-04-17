CC=g++
CFLAGS=-g -Wall -std=c++11
CV_FLAGS= `pkg-config --cflags --libs opencv`
INCLUDES= -I "./header"
LIBS=-lm
SHELL=/bin/sh
OBJECTS:= $(wildcard ./src/*.cpp)

# @echo $(OBJECTS)
all: blur_test opencv_test
blur_test: test/test_blur.cpp ${OBJECTS}
	${CC} ${CFLAGS} ${INCLUDES} -o $@ test/test_blur.cpp ${OBJECTS} ${CV_FLAGS} ${LIBS}
opencv_test: test/test_opencv.cpp
	${CC} ${CFLAGS} -o $@ test/test_opencv.cpp ${CV_FLAGS} ${LIBS}
.cpp.o:
	${CC} ${CFLAGS} ${INCLUDES} -c $<

.PHONY: clean
clean :
	-rm -f *.o core *.core opencv_test blur_test