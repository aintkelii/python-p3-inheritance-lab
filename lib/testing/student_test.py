#!/usr/bin/env python3

from student import Student
from user import User
        
class TestStudent:
    '''Class "Student" in student.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert(User in Student.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        
    def test_initializes_with_knowledge(self):
        '''initializes with empty list attribute "knowledge".'''
       

    def test_can_learn(self):
        '''learns from a string and adds to self.knowledge.'''
      