cppflag = -lopencv_core -lopencv_imgcodecs -lopencv_features2d

brisk.o: brisk.cpp
	g++ brisk.cpp $(cppflag) -o brisk.o -g

.PHONY: clean
clean:
	rm -f *.o
