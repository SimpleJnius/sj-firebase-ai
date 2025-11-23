from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaField,
    JavaMethod
)
from sjfirebaseai import package_path

__all__ = ("GenerationConfigBuilder", )


class GenerationConfigBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/GenerationConfig$Builder"

    # Public fields
    temperature = JavaField("Ljava/lang/Float;")
    topK = JavaField("Ljava/lang/Integer;")
    topP = JavaField("Ljava/lang/Float;")
    candidateCount = JavaField("Ljava/lang/Integer;")
    maxOutputTokens = JavaField("Ljava/lang/Integer;")
    presencePenalty = JavaField("Ljava/lang/Float;")
    frequencyPenalty = JavaField("Ljava/lang/Float;")
    stopSequences = JavaField("Ljava/util/List;")
    responseMimeType = JavaField("Ljava/lang/String;")
    responseSchema = JavaField(f"L{package_path}/type/Schema;")
    responseModalities = JavaField("Ljava/util/List;")
    thinkingConfig = JavaField(f"L{package_path}/type/ThinkingConfig;")

    # Builder methods (setters) returning GenerationConfig$Builder
    setTemperature = JavaMethod(f"(Ljava/lang/Float;)L{package_path}/type/GenerationConfig$Builder;")
    setTopK = JavaMethod(f"(Ljava/lang/Integer;)L{package_path}/type/GenerationConfig$Builder;")
    setTopP = JavaMethod(f"(Ljava/lang/Float;)L{package_path}/type/GenerationConfig$Builder;")
    setCandidateCount = JavaMethod(f"(Ljava/lang/Integer;)L{package_path}/type/GenerationConfig$Builder;")
    setMaxOutputTokens = JavaMethod(f"(Ljava/lang/Integer;)L{package_path}/type/GenerationConfig$Builder;")
    setPresencePenalty = JavaMethod(f"(Ljava/lang/Float;)L{package_path}/type/GenerationConfig$Builder;")
    setFrequencyPenalty = JavaMethod(f"(Ljava/lang/Float;)L{package_path}/type/GenerationConfig$Builder;")
    setStopSequences = JavaMethod(f"(Ljava/util/List;)L{package_path}/type/GenerationConfig$Builder;")
    setResponseMimeType = JavaMethod(f"(Ljava/lang/String;)L{package_path}/type/GenerationConfig$Builder;")
    setResponseSchema = JavaMethod(f"(L{package_path}/type/Schema;)L{package_path}/type/GenerationConfig$Builder;")
    setResponseModalities = JavaMethod(f"(Ljava/util/List;)L{package_path}/type/GenerationConfig$Builder;")
    setThinkingConfig = JavaMethod(f"(L{package_path}/type/ThinkingConfig;)"
                                   f"L{package_path}/type/GenerationConfig$Builder;")

    build = JavaMethod(f"()L{package_path}/type/GenerationConfig;")
