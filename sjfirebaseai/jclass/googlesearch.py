"""
Python binding for the Firebase AI GoogleSearch class.

This module provides a PyJNIus binding for the com.google.firebase.ai.type.GoogleSearch Java class.
It allows Python code to interact with Firebase AI GoogleSearch objects, which are used to
provide search capabilities to generative models.

The GoogleSearch class is a simple class that represents Google Search capabilities that can
be provided to a generative model through a Tool object.
"""

from jnius import (
    JavaClass,
    MetaJavaClass
)

__all__ = ("GoogleSearch",)


class GoogleSearch(JavaClass, metaclass=MetaJavaClass):
    """
    Python binding for the com.google.firebase.ai.type.GoogleSearch Java class.
    
    This class provides a PyJNIus implementation to the Firebase AI GoogleSearch class, which is used
    to provide Google Search capabilities to generative models through a Tool object.
    
    The GoogleSearch class is a simple class with a default constructor that creates an instance
    representing Google Search capabilities.
    """
    __javaclass__ = "com/google/firebase/ai/type/GoogleSearch"
