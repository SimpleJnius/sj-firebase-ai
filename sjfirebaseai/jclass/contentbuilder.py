from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod, JavaField
)
from sjfirebaseai import package_path

__all__ = ("ContentBuilder", )


class ContentBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/Content$Builder"
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
