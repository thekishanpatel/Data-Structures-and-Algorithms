CS 610 Spring 2019
Performance of Skip Lists
Course Project Option 1

The goal of this project is to analyze the performance of Skip List implementation of Ordered Dictionary ADT.

First define an interface for Ordered Dictionary ADT with the required methods and then provide the Skip list implementation.   You should give your own implementation of Skip list (not borrowed from any web site or from anyone else).

Second part of the project requires you to write a program to test the performance of this implementation for findElement, insertElement, removeElement, closestKeyAfter operations. Specifically, you should generate randomly a sequence of unique integers in a range (say 1 to 100000) to be inserted as keys starting from an empty ADT. You should intersperse insert operations with equal number of findElement, removeElement and closestKeyAfter operations in the sequence.  You should make sure there will be sufficient successful and unsuccessful searches and valid delete operations. One approach is as follows  : Suppose you have a “findElement” operation as m-th operation in the sequence and let k_(1,) 〖< k〗_2  …  〖≤ k〗_m be the keys inserted until then pick a number “t” randomly between 1 and 2m+1 and use key  k_l if t = 2l, key k_l-1 if t = 2l-1, for 1 ≤ l ≤ m and key k_(m ) + 1 if t = 2m+1. You can use same approach for “closestKeyAfter” operation. For “removeElement”, if k_(1,) 〖< k〗_2  …  〖< k〗_m be the keys inserted until then pick a number “t” randomly between 1 and m and choose key  k_l if t = l.

You should run this sequence of these operations many times and also keep statistics to measure average time for the four ADT operations as a function of number of keys in the tree at the time when operation was executed. This will enable you to plot the average time as a function of input size and make conclusions about the asymptotic growth of its performance (big-oh notation).

You should implement it in either C++ or Java (preferable). For Java, submit a zip file containing (a) source code, (b) Jar file containing .class files, (c) a Windows command file that I can run to test the first part of the project by entering a sequence of ADT operations with key values when prompted  and observing the skip list configuration printed by the program, (d) a Windows command file that I can run to execute the test program  of second part of the project and see the performance results in a tabular form and (e) one-page summary of your findings regarding the asymptotic complexity analysis of for the various ADT operations along with the performance graphs to support  your conclusions. For C++, instead of (b), submit the executables that can be run on an AFS UNIX host and for (c) and (d), submit Unix shell scripts to run the test programs.


