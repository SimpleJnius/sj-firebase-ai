from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod, autoclass
from sjfirebaseai import package_path

__all__ = ("FirebaseAI",)


class FirebaseAI(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/FirebaseVertexAI"

    getInstance = JavaMultipleMethod([
        (
            f"()L{package_path}/FirebaseAI;",
            True, False
        ),
        (
            f"(Lcom/google/firebase/FirebaseApp;"
            f"Lcom/google/firebase/ai/type/GenerativeBackend;)"
            f"L{package_path}/FirebaseAI;",
            True, False
        ),
        (
            "(Lcom/google/firebase/FirebaseApp;)"
            f"L{package_path}/FirebaseAI;",
            True, False
        ),
        (
            f"(Lcom/google/firebase/ai/type/GenerativeBackend;)"
            f"L{package_path}/FirebaseAI;",
            True, False
        )
    ])

    generativeModel = JavaMultipleMethod([
        (
            "(Ljava/lang/String;"
            f"L{package_path}/type/GenerationConfig;"
            "Ljava/util/List;"
            f"L{package_path}/type/RequestOptions;"
            f"Ljava/util/List;"
            f"L{package_path}/type/ToolConfig;"
            f"L{package_path}/type/Content;)"
            f"L{package_path}/GenerativeModel;",
            False, False
        ),
        (
            f"(Ljava/lang/String;"
            f"L{package_path}/type/GenerationConfig;"
            f"Ljava/util/List;"
            f"L{package_path}/type/RequestOptions;"
            f"Ljava/util/List;"
            f"L{package_path}/type/ToolConfig;)"
            f"L{package_path}/GenerativeModel;"
        ),
        (
            f"(Ljava/lang/String;"
            f"L{package_path}/type/GenerationConfig;"
            f"Ljava/util/List;"
            f"L{package_path}/type/RequestOptions;"
            f"Ljava/util/List;"
            f"L{package_path}/type/ToolConfig;)"
            f"L{package_path}/GenerativeModel;"
        ),
        (
            f"(Ljava/lang/String;"
            f"L{package_path}/type/GenerationConfig;"
            f"Ljava/util/List;"
            f"L{package_path}/type/RequestOptions;"
            f"Ljava/util/List;)"
            f"L{package_path}/GenerativeModel;"
        ),
        (
            f"(Ljava/lang/String;"
            f"L{package_path}/type/GenerationConfig;"
            f"Ljava/util/List;"
            f"L{package_path}/type/RequestOptions;)"
            f"L{package_path}/GenerativeModel;"
        ),
        (
            f"(Ljava/lang/String;"
            f"L{package_path}/type/GenerationConfig;"
            f"Ljava/util/List;)"
            f"L{package_path}/GenerativeModel;"
        ),
        (
            f"(Ljava/lang/String;"
            f"L{package_path}/type/GenerationConfig;)"
            f"L{package_path}/GenerativeModel;"
        ),
        (
            f"(Ljava/lang/String;)"
            f"L{package_path}/GenerativeModel;"
        ),
    ])
