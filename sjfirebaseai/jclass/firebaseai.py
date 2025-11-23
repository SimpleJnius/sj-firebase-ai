"""
Python binding for the Firebase AI main class.

This module provides a PyJNIus binding for the com.google.firebase.ai.FirebaseAI Java class.
It allows Python code to interact with Firebase AI services, including generative models,
live models, and imagen models.

The FirebaseAI class is the main entry point for Firebase AI functionality and provides
methods for creating and configuring different types of AI models.
"""

from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod, JavaStaticField, autoclass
from sjfirebaseai import package_path

__all__ = ("FirebaseAI",)


class FirebaseAI(JavaClass, metaclass=MetaJavaClass):
    """
    Python binding for the com.google.firebase.ai.FirebaseAI Java class.
    
    This class is the main entry point for Firebase AI functionality and provides
    methods for creating and configuring different types of AI models, including:
    - Generative models for text generation
    - Live models for real-time interaction
    - Imagen models for image generation
    
    The class follows the singleton pattern with static getInstance() methods
    for obtaining instances with different configurations.
    """
    __javaclass__ = f"{package_path}/FirebaseAI"
    
    # Constructor
    __javaconstructor__ = (
        "(Lcom/google/firebase/FirebaseApp;"
        "Lcom/google/firebase/ai/type/GenerativeBackend;"
        "Lkotlin/coroutines/CoroutineContext;"
        "Lcom/google/firebase/inject/Provider;"
        "Lcom/google/firebase/inject/Provider;)V"
    )
    """
    Constructor for the FirebaseAI class.
    
    Parameters:
        firebaseApp: The FirebaseApp instance.
        generativeBackend: The GenerativeBackend to use.
        coroutineContext: The Kotlin coroutine context.
        appCheckTokenProvider: Provider for the app check token.
        authProvider: Provider for the authentication.
    """
    
    # Companion object
    Companion = JavaStaticField('Lcom/google/firebase/ai/FirebaseAI$Companion;')
    """Static companion object for the FirebaseAI class that provides factory methods."""

    getInstance = JavaMultipleMethod([
        (
            f"()Lcom/google/firebase/ai/FirebaseAI;",
            True, False
        ),
        (
            f"(Lcom/google/firebase/FirebaseApp;"
            f"Lcom/google/firebase/ai/type/GenerativeBackend;)"
            f"Lcom/google/firebase/ai/FirebaseAI;",
            True, False
        ),
        (
            "(Lcom/google/firebase/FirebaseApp;)"
            f"Lcom/google/firebase/ai/FirebaseAI;",
            True, False
        ),
        (
            f"(Lcom/google/firebase/ai/type/GenerativeBackend;)"
            f"Lcom/google/firebase/ai/FirebaseAI;",
            True, False
        )
    ])
    """
    Static factory methods for getting FirebaseAI instances.
    
    These methods follow the singleton pattern and provide different ways to obtain
    a FirebaseAI instance with various configurations.
    
    Overloaded methods:
    1. getInstance(): Gets the default FirebaseAI instance.
    2. getInstance(firebaseApp, generativeBackend): Gets a FirebaseAI instance with the specified
       FirebaseApp and GenerativeBackend.
    3. getInstance(firebaseApp): Gets a FirebaseAI instance with the specified FirebaseApp.
    4. getInstance(generativeBackend): Gets a FirebaseAI instance with the specified GenerativeBackend.
    
    Returns:
        A FirebaseAI instance configured according to the parameters.
    """

    generativeModel = JavaMultipleMethod([
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/GenerationConfig;"
            "Ljava/util/List;"
            "Ljava/util/List;"
            "Lcom/google/firebase/ai/type/ToolConfig;"
            "Lcom/google/firebase/ai/type/Content;"
            "Lcom/google/firebase/ai/type/RequestOptions;)"
            "Lcom/google/firebase/ai/GenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/GenerationConfig;"
            "Ljava/util/List;"
            "Ljava/util/List;"
            "Lcom/google/firebase/ai/type/ToolConfig;"
            "Lcom/google/firebase/ai/type/Content;)"
            "Lcom/google/firebase/ai/GenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/GenerationConfig;"
            "Ljava/util/List;"
            "Ljava/util/List;"
            "Lcom/google/firebase/ai/type/ToolConfig;)"
            "Lcom/google/firebase/ai/GenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/GenerationConfig;"
            "Ljava/util/List;"
            "Ljava/util/List;)"
            "Lcom/google/firebase/ai/GenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/GenerationConfig;"
            "Ljava/util/List;)"
            "Lcom/google/firebase/ai/GenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/GenerationConfig;)"
            "Lcom/google/firebase/ai/GenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;)"
            "Lcom/google/firebase/ai/GenerativeModel;",
            False, False
        ),
    ])
    """
    Creates a generative model with the specified configuration.
    
    These methods create GenerativeModel instances with various configurations for
    text generation and other AI tasks.
    
    Overloaded methods:
    1. generativeModel(modelName, config, safetySettings, tools, toolConfig, content, requestOptions):
       Creates a generative model with all configuration options.
    2. generativeModel(modelName, config, safetySettings, tools, toolConfig, content):
       Creates a generative model with model name, generation config, safety settings, tools, tool config, and content.
    3. generativeModel(modelName, config, safetySettings, tools, toolConfig):
       Creates a generative model with model name, generation config, safety settings, tools, and tool config.
    4. generativeModel(modelName, config, safetySettings, tools):
       Creates a generative model with model name, generation config, safety settings, and tools.
    5. generativeModel(modelName, config, safetySettings):
       Creates a generative model with model name, generation config, and safety settings.
    6. generativeModel(modelName, config):
       Creates a generative model with model name and generation config.
    7. generativeModel(modelName):
       Creates a generative model with just the model name.
    
    Parameters:
        modelName: The name of the model to use.
        config: The generation configuration.
        safetySettings: List of safety settings to apply.
        tools: List of tools available to the model.
        toolConfig: Configuration for tool usage.
        content: Initial content for the model.
        requestOptions: Additional options for the request.
    
    Returns:
        A GenerativeModel instance configured according to the parameters.
    """
    
    liveModel = JavaMultipleMethod([
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/LiveGenerationConfig;"
            "Ljava/util/List;"
            "Lcom/google/firebase/ai/type/Content;"
            "Lcom/google/firebase/ai/type/RequestOptions;)"
            "Lcom/google/firebase/ai/LiveGenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/LiveGenerationConfig;"
            "Ljava/util/List;"
            "Lcom/google/firebase/ai/type/Content;)"
            "Lcom/google/firebase/ai/LiveGenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/LiveGenerationConfig;"
            "Ljava/util/List;)"
            "Lcom/google/firebase/ai/LiveGenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/LiveGenerationConfig;)"
            "Lcom/google/firebase/ai/LiveGenerativeModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;)"
            "Lcom/google/firebase/ai/LiveGenerativeModel;",
            False, False
        ),
    ])
    """
    Creates a live generative model with the specified configuration.
    
    These methods create LiveGenerativeModel instances with various configurations for
    real-time interaction with AI models.
    
    Overloaded methods:
    1. liveModel(modelName, config, tools, content, requestOptions):
       Creates a live model with all configuration options.
    2. liveModel(modelName, config, tools, content):
       Creates a live model with model name, generation config, tools, and content.
    3. liveModel(modelName, config, tools):
       Creates a live model with model name, generation config, and tools.
    4. liveModel(modelName, config):
       Creates a live model with model name and generation config.
    5. liveModel(modelName):
       Creates a live model with just the model name.
    
    Parameters:
        modelName: The name of the model to use.
        config: The live generation configuration.
        tools: List of tools available to the model.
        content: Initial content for the model.
        requestOptions: Additional options for the request.
    
    Returns:
        A LiveGenerativeModel instance configured according to the parameters.
    """
    
    imagenModel = JavaMultipleMethod([
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/ImagenGenerationConfig;"
            "Lcom/google/firebase/ai/type/ImagenSafetySettings;"
            "Lcom/google/firebase/ai/type/RequestOptions;)"
            "Lcom/google/firebase/ai/ImagenModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/ImagenGenerationConfig;"
            "Lcom/google/firebase/ai/type/ImagenSafetySettings;)"
            "Lcom/google/firebase/ai/ImagenModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;"
            "Lcom/google/firebase/ai/type/ImagenGenerationConfig;)"
            "Lcom/google/firebase/ai/ImagenModel;",
            False, False
        ),
        (
            "(Ljava/lang/String;)"
            "Lcom/google/firebase/ai/ImagenModel;",
            False, False
        ),
    ])
    """
    Creates an imagen model with the specified configuration.
    
    These methods create ImagenModel instances with various configurations for
    image generation tasks.
    
    Overloaded methods:
    1. imagenModel(modelName, config, safetySettings, requestOptions):
       Creates an imagen model with all configuration options.
    2. imagenModel(modelName, config, safetySettings):
       Creates an imagen model with model name, generation config, and safety settings.
    3. imagenModel(modelName, config):
       Creates an imagen model with model name and generation config.
    4. imagenModel(modelName):
       Creates an imagen model with just the model name.
    
    Parameters:
        modelName: The name of the model to use.
        config: The imagen generation configuration.
        safetySettings: Safety settings to apply to image generation.
        requestOptions: Additional options for the request.
    
    Returns:
        An ImagenModel instance configured according to the parameters.
    """
