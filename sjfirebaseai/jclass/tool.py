"""
Python binding for the Firebase AI Tool class.

This module provides a PyJNIus binding for the com.google.firebase.ai.type.Tool Java class.
It allows Python code to interact with Firebase AI Tool objects, which are used to define
tools that can be used by generative models, such as function declarations and Google Search.

The Tool class provides methods for creating tools with function declarations or Google Search
capabilities.
"""

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaStaticMethod,
    JavaStaticField
)

__all__ = ("Tool",)


class Tool(JavaClass, metaclass=MetaJavaClass):
    """
    Python binding for the com.google.firebase.ai.type.Tool Java class.
    
    This class provides a PyJNIus interface to the Firebase AI Tool class, which is used
    to define tools that can be used by generative models, such as function declarations
    and Google Search capabilities.
    
    The Tool class includes methods for creating tools with function declarations or
    Google Search capabilities.
    """
    __javaclass__ = "com/google/firebase/ai/type/Tool"

    # Constructor
    __javaconstructor__ = [
        ('(Ljava/util/List;Lcom/google/firebase/ai/type/GoogleSearch;)V', False)
    ]
    """
    Java constructor for the Tool class.

    Parameters:
        functionDeclarations: A list of FunctionDeclaration objects that define the functions
                             available to the model.
        googleSearch: A GoogleSearch object that provides search capabilities to the model.
    """
    
    # Companion object
    Companion = JavaStaticField('Lcom/google/firebase/ai/type/Tool$Companion;')
    """Static companion object for the Tool class that provides factory methods."""
    
    # Static methods
    functionDeclarations = JavaStaticMethod('(Ljava/util/List;)Lcom/google/firebase/ai/type/Tool;')
    """
    Creates a Tool with function declarations.
    
    This method creates a Tool object that provides function declarations to the model.
    
    Parameters:
        functionDeclarations: A list of FunctionDeclaration objects that define the functions
                             available to the model.
    
    Returns:
        A Tool object with the specified function declarations.
    """
    
    googleSearch = JavaStaticMethod('(Lcom/google/firebase/ai/type/GoogleSearch;)Lcom/google/firebase/ai/type/Tool;')
    """
    Creates a Tool with Google Search capabilities.
    
    This method creates a Tool object that provides Google Search capabilities to the model.
    
    Parameters:
        googleSearch: A GoogleSearch object that provides search capabilities to the model.
    
    Returns:
        A Tool object with Google Search capabilities.
    """