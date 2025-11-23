from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaStaticMethod,
    JavaMethod,
    JavaMultipleMethod
)
from sjfirebaseai import package_path

__all__ = ("GenerativeModelFutures", )


class GenerativeModelFutures(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/java/GenerativeModelFutures"

    generateContent = JavaMethod(
        "(Lcom/google/firebase/ai/type/Content;[Lcom/google/firebase/ai/type/Content;)"
        f"Lcom/google/common/util/concurrent/ListenableFuture;",
        varargs=True
    )

    generateContentStream = JavaMethod(
        "(Lcom/google/firebase/ai/type/Content;[Lcom/google/firebase/ai/type/Content;)"
        f"Lorg/reactivestreams/Publisher;",
        varargs=True
    )

    countTokens = JavaMethod(
        "(Lcom/google/firebase/ai/type/Content;[Lcom/google/firebase/ai/type/Content;)"
        f"Lcom/google/common/util/concurrent/ListenableFuture;",
        varargs=True
    )

    startChat = JavaMultipleMethod([
        (
            f"()L{package_path}/java/ChatFutures;",
            False, False
        ),
        (
            f"(Ljava/util/List;)"
            f"L{package_path}/java/ChatFutures;",
            False, False
        )
    ])

    getGenerativeModel = JavaMethod(f"()L{package_path}/GenerativeModel;")

    from_ = JavaStaticMethod(
        f"(L{package_path}/GenerativeModel;)"
        f"L{package_path}/java/GenerativeModelFutures;"
    )
    locals()["from"] = from_
