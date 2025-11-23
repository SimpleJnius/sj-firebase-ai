from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaStaticMethod,
    JavaMultipleMethod
)
from sjfirebaseai import package_path

__all__ = ("GenerativeBackend", )


class GenerativeBackend(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/GenerativeBackend"
    __javaconstructor__ = (
        "(Ljava/lang/String;"
        "Lcom/google/firebase/ai/type/GenerativeBackendEnum;)V"
    )
    googleAI = JavaStaticMethod("()Lcom/google/firebase/ai/type/GenerativeBackend;")
    vertexAI = JavaMultipleMethod([
        (
            f"(Ljava/lang/String;)Lcom/google/firebase/ai/type/GenerativeBackend;",
            True, False
        ),
        (
            "()Lcom/google/firebase/ai/type/GenerativeBackend;",
            True, False
        )
    ])
