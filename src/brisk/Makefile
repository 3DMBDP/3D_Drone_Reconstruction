cppflag = -lopencv_core -lopencv_imgcodecs

brisk.o: brisk.cpp
	g++ brisk.cpp $(cppflag) -o brisk.o

.PHONY: clean
clean:
	rm -f *.o
