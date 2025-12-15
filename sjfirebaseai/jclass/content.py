"""
Python binding for the Firebase AI Content class.

This module provides a PyJNIus binding for the
com.google.firebase.ai.type.Content Java/Kotlin class. It allows Python
code to construct Content objects and access their public fields.

Constructors supported:
- Content(String role, List<? extends Part> parts)
- Content(String, List, int, kotlin.jvm.internal.DefaultConstructorMarker)
- Content(List<? extends Part> parts)

Public methods exposed:
- getRole(): String
- getParts(): List<Part>
- copy(String role, List<? extends Part>): Content

Note: Kotlin internal methods with a "$" in their names (e.g.,
copy$default, toInternal$com_google_firebase_firebase_ai) are not
exposed in this wrapper.
"""

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod, JavaField,
)

__all__ = ("Content",)


class Content(JavaClass, metaclass=MetaJavaClass):
    """Python binding for com.google.firebase.ai.type.Content."""

    __javaclass__ = "com/google/firebase/ai/type/Content"

    # Constructors (primary, synthetic with DefaultConstructorMarker, and
    # convenience constructor that takes only parts)
    __javaconstructor__ = [
        (
            "(Ljava/lang/String;Ljava/util/List;)V",
            False,
        ),
        (
            "(Ljava/lang/String;Ljava/util/List;ILkotlin/jvm/internal/DefaultConstructorMarker;)V",
            False,
        ),
        (
            "(Ljava/util/List;)V",
            False,
        ),
    ]

    # Getters
    getRole = JavaMethod("()Ljava/lang/String;")
    getParts = JavaMethod("()Ljava/util/List;")

    # Copy method
    copy = JavaMethod(
        "(Ljava/lang/String;Ljava/util/List;)Lcom/google/firebase/ai/type/Content;"
    )

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = f"com/google/firebase/ai/type/Content$Builder"
        role = JavaField("Ljava/lang/String;")
        parts = JavaField("Ljava/util/List;")
        setRole = JavaMethod("(Ljava/lang/String;)Lcom/google/firebase/ai/type/Content$Builder;")
        setParts = JavaMethod("(Ljava/util/List;)Lcom/google/firebase/ai/type/Content$Builder;")
        addPart = JavaMethod(
            "(Lcom/google/firebase/ai/type/Part;)"
            "Lcom/google/firebase/ai/type/Content$Builder;"
        )
        addText = JavaMethod(
            "(Ljava/lang/String;)"
            "Lcom/google/firebase/ai/type/Content$Builder;"
        )
        addInlineData = JavaMethod(
            "([BLjava/lang/String;)"
            "Lcom/google/firebase/ai/type/Content$Builder;"
        )
        addImage = JavaMethod(
            "(Landroid/graphics/Bitmap;)"
            "Lcom/google/firebase/ai/type/Content$Builder;"
        )
        addFileData = JavaMethod(
            "(Ljava/lang/String;Ljava/lang/String;)"
            "Lcom/google/firebase/ai/type/Content$Builder;"
        )
        build = JavaMethod(f"()Lcom/google/firebase/ai/type/Content;")
