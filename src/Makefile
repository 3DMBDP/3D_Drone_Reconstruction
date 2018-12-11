cppflag = `pkg-config --cflags --libs opencv` -lopencv_sfm

reconstruction.o: reconstruction.cpp
	g++ reconstruction.cpp $(cppflag) -o reconstruction.o -g

.PHONY: clean run
run:
	./reconstruction.o
clean:
	rm -f *.o
