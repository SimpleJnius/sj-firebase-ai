"""
Python binding for the Firebase AI GenerationConfig.Builder class.

This module provides a PyJNIus binding for the com.google.firebase.ai.type.GenerationConfig$Builder Java class.
It allows Python code to configure generation parameters for Firebase AI models, such as
temperature, top-k, top-p, and other settings that control the text generation process.

The Builder class follows the builder pattern and provides methods for setting various
generation parameters and building a GenerationConfig object.
"""

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod,
    JavaField
)

__all__ = ("GenerationConfigBuilder",)

    
class GenerationConfigBuilder(JavaClass, metaclass=MetaJavaClass):
    """
    Python binding for the com.google.firebase.ai.type.GenerationConfig$Builder Java class.

    This class follows the builder pattern and provides methods for setting various
    generation parameters and building a GenerationConfig object.

    The builder allows configuration of parameters such as temperature, top-k, top-p,
    and other settings that control the text generation process.
    """
    __javaclass__ = "com/google/firebase/ai/type/GenerationConfig$Builder"

    # Public fields
    temperature = JavaField('Ljava/lang/Float;')
    """
    Controls randomness in the output. Higher values (e.g., 0.8) make the output more random,
    while lower values (e.g., 0.2) make it more focused and deterministic.
    """

    topK = JavaField('Ljava/lang/Integer;')
    """
    Limits the token selection to the top K most probable tokens at each step.
    A higher value allows more diversity, while a lower value makes the output more focused.
    """

    topP = JavaField('Ljava/lang/Float;')
    """
    Limits the token selection to a subset of tokens with a cumulative probability of at most P.
    Also known as nucleus sampling.
    """

    candidateCount = JavaField('Ljava/lang/Integer;')
    """
    The number of candidate responses to generate.
    """

    maxOutputTokens = JavaField('Ljava/lang/Integer;')
    """
    The maximum number of tokens to generate in the response.
    """

    presencePenalty = JavaField('Ljava/lang/Float;')
    """
    Penalizes tokens based on whether they appear in the text so far.
    Higher values increase the likelihood of generating new topics.
    """

    frequencyPenalty = JavaField('Ljava/lang/Float;')
    """
    Penalizes tokens based on their frequency in the text so far.
    Higher values decrease the likelihood of repeating the same tokens.
    """

    stopSequences = JavaField('Ljava/util/List;')
    """
    A list of strings that, if generated, will cause the model to stop generating further tokens.
    """

    responseMimeType = JavaField('Ljava/lang/String;')
    """
    The MIME type of the expected response (e.g., "text/plain", "application/json").
    """

    responseSchema = JavaField('Lcom/google/firebase/ai/type/Schema;')
    """
    A Schema object that defines the structure of the expected response.
    """

    responseModalities = JavaField('Ljava/util/List;')
    """
    A list of ResponseModality objects that define the modalities of the expected response.
    """

    thinkingConfig = JavaField('Lcom/google/firebase/ai/type/ThinkingConfig;')
    """
    Configuration for the model's thinking process.
    """

    # Setter methods
    setTemperature = JavaMethod('(Ljava/lang/Float;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the temperature parameter for controlling randomness in the output.
    
    Parameters:
        temperature: A Float value. Higher values (e.g., 0.8) make the output more random,
                     while lower values (e.g., 0.2) make it more focused and deterministic.
    
    Returns:
        This Builder instance for method chaining.
    """

    setTopK = JavaMethod('(Ljava/lang/Integer;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the top-k parameter for token selection.
    
    Parameters:
        topK: An Integer value that limits the token selection to the top K most probable tokens
              at each step. A higher value allows more diversity, while a lower value makes
              the output more focused.
    
    Returns:
        This Builder instance for method chaining.
    """

    setTopP = JavaMethod('(Ljava/lang/Float;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the top-p parameter for nucleus sampling.
    
    Parameters:
        topP: A Float value that limits the token selection to a subset of tokens with a
              cumulative probability of at most P. Also known as nucleus sampling.
    
    Returns:
        This Builder instance for method chaining.
    """

    setCandidateCount = JavaMethod('(Ljava/lang/Integer;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the number of candidate responses to generate.
    
    Parameters:
        candidateCount: An Integer value representing the number of candidate responses to generate.
    
    Returns:
        This Builder instance for method chaining.
    """

    setMaxOutputTokens = JavaMethod('(Ljava/lang/Integer;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the maximum number of tokens to generate in the response.
    
    Parameters:
        maxOutputTokens: An Integer value representing the maximum number of tokens to generate.
    
    Returns:
        This Builder instance for method chaining.
    """

    setPresencePenalty = JavaMethod('(Ljava/lang/Float;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the presence penalty parameter.
    
    Parameters:
        presencePenalty: A Float value that penalizes tokens based on whether they appear in the
                         text so far. Higher values increase the likelihood of generating new topics.
    
    Returns:
        This Builder instance for method chaining.
    """

    setFrequencyPenalty = JavaMethod('(Ljava/lang/Float;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the frequency penalty parameter.
    
    Parameters:
        frequencyPenalty: A Float value that penalizes tokens based on their frequency in the
                          text so far. Higher values decrease the likelihood of repeating the same tokens.
    
    Returns:
        This Builder instance for method chaining.
    """

    setStopSequences = JavaMethod('(Ljava/util/List;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the stop sequences for the generation.
    
    Parameters:
        stopSequences: A List of strings that, if generated, will cause the model to stop
                       generating further tokens.
    
    Returns:
        This Builder instance for method chaining.
    """

    setResponseMimeType = JavaMethod('(Ljava/lang/String;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the MIME type of the expected response.
    
    Parameters:
        responseMimeType: A String representing the MIME type of the expected response
                          (e.g., "text/plain", "application/json").
    
    Returns:
        This Builder instance for method chaining.
    """

    setResponseSchema = JavaMethod('(Lcom/google/firebase/ai/type/Schema;)'
                                   'Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the schema for the expected response.
    
    Parameters:
        responseSchema: A Schema object that defines the structure of the expected response.
    
    Returns:
        This Builder instance for method chaining.
    """

    setResponseModalities = JavaMethod('(Ljava/util/List;)Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the modalities of the expected response.
    
    Parameters:
        responseModalities: A List of ResponseModality objects that define the modalities
                            of the expected response.
    
    Returns:
        This Builder instance for method chaining.
    """

    setThinkingConfig = JavaMethod('(Lcom/google/firebase/ai/type/ThinkingConfig;)'
                                   'Lcom/google/firebase/ai/type/GenerationConfig$Builder;')
    """
    Sets the thinking configuration.
    
    Parameters:
        thinkingConfig: A ThinkingConfig object that configures the model's thinking process.
    
    Returns:
        This Builder instance for method chaining.
    """

    build = JavaMethod('()Lcom/google/firebase/ai/type/GenerationConfig;')
    """
    Builds a GenerationConfig object with the configured parameters.
    
    Returns:
        A GenerationConfig object with the parameters set on this builder.
    """