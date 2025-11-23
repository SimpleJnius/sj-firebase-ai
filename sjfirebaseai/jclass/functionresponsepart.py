"""
Python binding for the Firebase AI FunctionResponsePart class.

This module provides a PyJNIus binding for the
com.google.firebase.ai.type.FunctionResponsePart Java/Kotlin class.
It allows Python code to construct FunctionResponsePart objects and
access their public fields.

Constructors supported:
- FunctionResponsePart(String name, JsonObject response, String id)
- FunctionResponsePart(String, JsonObject, String, int,
  kotlin.jvm.internal.DefaultConstructorMarker)
- FunctionResponsePart(String name, JsonObject response)

Public methods exposed:
- getName(): String
- getResponse(): kotlinx.serialization.json.JsonObject
- getId(): String

Note: Kotlin internal methods with a "$" in their names (e.g.,
toInternalFunctionCall$com_google_firebase_firebase_ai) are not exposed
in this wrapper.
"""

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod,
)

__all__ = ("FunctionResponsePart",)


class FunctionResponsePart(JavaClass, metaclass=MetaJavaClass):
    """Python binding for com.google.firebase.ai.type.FunctionResponsePart."""

    __javaclass__ = "com/google/firebase/ai/type/FunctionResponsePart"

    # Constructors (primary, synthetic with DefaultConstructorMarker, and
    # convenience constructor without id)
    __javaconstructor__ = [
        (
            "(Ljava/lang/String;Lkotlinx/serialization/json/JsonObject;Ljava/lang/String;)V",
            False,
        ),
        (
            "(Ljava/lang/String;Lkotlinx/serialization/json/JsonObject;Ljava/lang/String;ILkotlin/jvm/internal/DefaultConstructorMarker;)V",
            False,
        ),
        (
            "(Ljava/lang/String;Lkotlinx/serialization/json/JsonObject;)V",
            False,
        ),
    ]

    # Public getters
    getName = JavaMethod("()Ljava/lang/String;")
    getResponse = JavaMethod(
        "()Lkotlinx/serialization/json/JsonObject;"
    )
    getId = JavaMethod("()Ljava/lang/String;")
