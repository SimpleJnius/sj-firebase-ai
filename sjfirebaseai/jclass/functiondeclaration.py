"""
Python binding for the Firebase AI FunctionDeclaration class.

This module provides a PyJNIus binding for the com.google.firebase.ai.type.FunctionDeclaration
Java/Kotlin class. It allows Python code to construct FunctionDeclaration objects and access
its fields as defined by the Firebase AI SDK.

Constructors supported:
- FunctionDeclaration(String name, String description,
  Map<String, Schema> parameters, List<String> optionalParameters)
- FunctionDeclaration(String, String, Map, List, int,
  kotlin.jvm.internal.DefaultConstructorMarker)
"""

from jnius import (
    JavaClass,
    MetaJavaClass,
)

__all__ = ("FunctionDeclaration",)


class FunctionDeclaration(JavaClass, metaclass=MetaJavaClass):
    """
    Python binding for com.google.firebase.ai.type.FunctionDeclaration
    """
    __javaclass__ = "com/google/firebase/ai/type/FunctionDeclaration"

    # Constructors (primary and synthetic with DefaultConstructorMarker)
    __javaconstructor__ = [
        (
            "(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;Ljava/util/List;)V",
            False,
        ),
        (
            "(Ljava/lang/String;"
            "Ljava/lang/String;"
            "Ljava/util/Map;"
            "Ljava/util/List;"
            "ILkotlin/jvm/internal/DefaultConstructorMarker;)V",
            False,
        ),
    ]

