#!/usr/bin/env python3

from teacher import Teacher
from user import User



class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert(User in Teacher.__bases__)

    
        '''initializes with first and last name.'''
      

    def test_has_attribute_knowledge(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        
    def test_can_teach(self):
        '''teaches from list of knowledge.'''
        