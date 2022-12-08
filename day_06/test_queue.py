from queue import queue
import pytest

def test_init_int():
    q = queue([1,2,3])
    assert len(q.items()) == 3

def test_init_char():
    q = queue(['a','b','c'])
    assert len(q.items()) == 3

def test_init_str():
    q = queue(['abc','def','ghi'])
    assert len(q.items()) == 3

def test_init_mix():
    q = queue([1,'a','ghi'])
    assert len(q.items()) == 3

def test_enqueue_empty():
    q = queue()
    q.enqueue(1)
    assert len(q.items()) == 1

def test_enqueue_init():
    q = queue([1,2,3])
    q.enqueue(4)
    assert q.items()[0] == 4
    assert len(q.items()) == 4

def test_dequeue():
    q = queue([1,2,3])
    assert q.dequeue() == 3
    assert q.dequeue() == 2
    assert q.dequeue() == 1
    assert q.dequeue() == None


