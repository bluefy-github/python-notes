"""
    进程
        进程是操作系统分配资源的最小单位, 未运行的代码可以称为程序, 一个运行中的程序就是一个进程, 进程拥有自己独立的内存空间, 进
    程间数据不共享, 进程的创建和切换开销大, 进程的数量不应过多, 最好和CPU核数相同, 不然进程切换带来的开销反而会降低性能.

    线程
        线程是CPU调度的最小单位, 依赖进程存在, 一个进程至少有一个线程, 同一进程可以有多个线程, 彼此共享内存, 线程开销比进程小,
    由操作系统负责调度, 线程的数量不是越多越好, 线程过多也会导致性能的下降.

    协程
        协程是一种用户态的轻量级线程, 协程运行在一个线程中, 协程的切换由用户自己控制, 协程切换的开销比线程小很多, 协程切换只需要
    保存寄存器上下文和栈, 而线程的切换远不止这些, 理论上协程可以有上百万个; 协程可以不加锁的访问全局变量, 因此可以减少锁管理带来
    的额外开销, 但需要注意的是, 并不是说协程就不需要锁机制了, 比如获取数据库连接操作, 并不需要每个协程都连接一次.


    有了协程多线程还有存在的意义么?
    个人认为python的多线程是有必要的。并发并发具体是对指线程（或者协程）的调度。
    python的线程间切换主要是语言层面上的（GIL）。
    早期的线程间切换主要考量线程已经运行的字节码个数（达到一个阈值后，释放GIL，把控制权交给其他线程），
    后面改成了考量线程运行的时长（类似时间片）。
    [1]python的协程间切换主要是应用层面上的。调度的好坏是多维度的，不仅取决于对公共资源的控制权的精确性，
    也取决于公平性。对于io阻塞的操作，协程相较于线程，能更精确的获取（或者释放）对资源的控制权。
    这是因为用户层相较于语言层，用户层能更好的感知特定操作的时机。对于非io阻塞的操作，线程相较于协程，
    能更公平的分配对资源的控制权。这是因为语言层相较于用户层，语言层能更好的感知到多个线程的运行状态，
    并在掌握更多信息的前提下（线程运行的字节码和时长），进行更加合理的GIL的获取和释放。
    并行虽然在python层面上，有GIL的限制，但是当python调用C扩展的时候，可以在C扩展中把GIL释放掉，
    从而达到使用多线程并行的目的。
    [2]当下许多的机器学习，深度学习等高性能计算框架，都会在调用C扩展的时候，释放掉GIL。


"""
import asyncio
