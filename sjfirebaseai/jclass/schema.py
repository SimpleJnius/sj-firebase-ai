"""
Python binding for the Firebase AI Schema class.

This module provides a PyJNIus binding for the com.google.firebase.ai.type.Schema Java class.
It allows Python code to interact with Firebase AI Schema objects, which are used to define
the structure and validation rules for data in Firebase AI applications.

The Schema class provides methods for creating various types of schemas (boolean, numeric,
string, object, array, etc.) and for accessing schema properties.
"""

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaStaticMethod,
    JavaMultipleMethod,
    JavaMethod,
    JavaStaticField
)

__all__ = ("Schema",)


class Schema(JavaClass, metaclass=MetaJavaClass):
    """
    Python binding for the com.google.firebase.ai.type.Schema Java class.
    
    This class provides a PyJNIus interface to the Firebase AI Schema class, which is used
    to define the structure and validation rules for data in Firebase AI applications.
    It includes methods for creating various types of schemas (boolean, numeric, string,
    object, array, etc.) and for accessing schema properties.
    
    The Schema class follows the JSON Schema specification and provides a way to define
    the expected structure of JSON data, including types, formats, constraints, and
    nested objects.
    """
    __javaclass__ = "com/google/firebase/ai/type/Schema"
    
    # Constructors
    __javaconstructor__ = [
        (
            '(Ljava/lang/String;'
            'Ljava/lang/String;'
            'Ljava/lang/String;'
            'Ljava/lang/Boolean;'
            'Ljava/util/List;'
            'Ljava/util/Map;'
            'Ljava/util/List;'
            'Lcom/google/firebase/ai/type/Schema;'
            'Ljava/lang/String;'
            'Ljava/lang/Integer;'
            'Ljava/lang/Integer;'
            'Ljava/lang/Double;'
            'Ljava/lang/Double;'
            'Ljava/util/List;)V',
            False
        ),
        (
            '(Ljava/lang/String;'
            'Ljava/lang/String;'
            'Ljava/lang/String;'
            'Ljava/lang/Boolean;'
            'Ljava/util/List;'
            'Ljava/util/Map;'
            'Ljava/util/List;'
            'Lcom/google/firebase/ai/type/Schema;'
            'Ljava/lang/String;'
            'Ljava/lang/Integer;'
            'Ljava/lang/Integer;'
            'Ljava/lang/Double;'
            'Ljava/lang/Double;'
            'Ljava/util/List;'
            'ILkotlin/jvm/internal/DefaultConstructorMarker;)V',
            False
        )
    ]
    """
    Java constructors for the Schema class.
    
    The Schema class has two constructors:
    1. Primary constructor with 14 parameters for type, description, format, nullable, enum,
       properties, required, items, title, minItems, maxItems, minimum, maximum, and anyOf.
    2. Secondary constructor with additional DefaultConstructorMarker parameter used internally
       by Kotlin.
    """
    
    # Companion object
    Companion = JavaStaticField('Lcom/google/firebase/ai/type/Schema$Companion;')
    """Static companion object for the Schema class that provides factory methods."""
    
    # Field getters
    getType = JavaMethod('()Ljava/lang/String;')
    """
    Returns the data type of the schema (e.g., 'string', 'number', 'object', 'array', etc.).
    
    Getter methods provide access to the various properties of a Schema object,
    including type information, constraints, and nested schemas.
    """
    
    getDescription = JavaMethod('()Ljava/lang/String;')
    """Returns the description of the schema, providing human-readable documentation."""
    
    getFormat = JavaMethod('()Ljava/lang/String;')
    """Returns the format of the schema, specifying additional format information for the data type."""
    
    getNullable = JavaMethod('()Ljava/lang/Boolean;')
    """Returns whether the schema allows null values."""
    
    getEnum = JavaMethod('()Ljava/util/List;')
    """Returns a list of allowed values for the schema, if it's an enumeration."""
    
    getProperties = JavaMethod('()Ljava/util/Map;')
    """Returns a map of property names to schemas for object schemas."""
    
    getRequired = JavaMethod('()Ljava/util/List;')
    """Returns a list of required property names for object schemas."""
    
    getItems = JavaMethod('()Lcom/google/firebase/ai/type/Schema;')
    """Returns the schema for array items, if this schema is an array type."""
    
    getTitle = JavaMethod('()Ljava/lang/String;')
    """Returns the title of the schema, providing a short description."""
    
    getMinItems = JavaMethod('()Ljava/lang/Integer;')
    """Returns the minimum number of items for array schemas."""
    
    getMaxItems = JavaMethod('()Ljava/lang/Integer;')
    """Returns the maximum number of items for array schemas."""
    
    getMinimum = JavaMethod('()Ljava/lang/Double;')
    """Returns the minimum value for numeric schemas."""
    
    getMaximum = JavaMethod('()Ljava/lang/Double;')
    """Returns the maximum value for numeric schemas."""
    
    getAnyOf = JavaMethod('()Ljava/util/List;')
    """Returns a list of alternative schemas, any of which the data may conform to."""
    
    # Static methods - boolean
    boolean = JavaMultipleMethod([
        ('(Ljava/lang/String;ZLjava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('()Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating boolean schemas.
    
    These methods create Schema objects with type 'boolean' and various configurations.
    
    Creates a boolean schema.
    
    Overloaded methods:
    1. boolean(title, nullable, description): Creates a boolean schema with the specified title, 
       nullable flag, and description.
    2. boolean(title, nullable): Creates a boolean schema with the specified title and nullable flag.
    3. boolean(title): Creates a boolean schema with the specified title.
    4. boolean(): Creates a default boolean schema.
    
    Returns:
        A Schema object representing a boolean value.
    """
    
    # Static methods - numInt
    numInt = JavaMultipleMethod([
        ('(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Double;Ljava/lang/Double;)'
         'Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Double;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLjava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('()Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating integer schemas.
    
    These methods create Schema objects with type 'integer' and various configurations.
    
    Creates an integer schema.
    
    Overloaded methods:
    1. numInt(title, nullable, description, minimum, maximum): Creates an integer schema with the 
       specified title, nullable flag, description, minimum value, and maximum value.
    2. numInt(title, nullable, description, minimum): Creates an integer schema with the specified 
       title, nullable flag, description, and minimum value.
    3. numInt(title, nullable, description): Creates an integer schema with the specified title, 
       nullable flag, and description.
    4. numInt(title, nullable): Creates an integer schema with the specified title and nullable flag.
    5. numInt(title): Creates an integer schema with the specified title.
    6. numInt(): Creates a default integer schema.
    
    Returns:
        A Schema object representing an integer value.
    """
    
    # Static methods - numLong
    numLong = JavaMultipleMethod([
        ('(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Double;Ljava/lang/Double;)'
         'Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Double;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLjava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('()Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating long integer schemas.
    
    These methods create Schema objects with type 'integer' and format 'int64' for long integers.
    
    Creates a long integer schema.
    
    Overloaded methods:
    1. numLong(title, nullable, description, minimum, maximum): Creates a long integer schema with the 
       specified title, nullable flag, description, minimum value, and maximum value.
    2. numLong(title, nullable, description, minimum): Creates a long integer schema with the specified 
       title, nullable flag, description, and minimum value.
    3. numLong(title, nullable, description): Creates a long integer schema with the specified title, 
       nullable flag, and description.
    4. numLong(title, nullable): Creates a long integer schema with the specified title and nullable flag.
    5. numLong(title): Creates a long integer schema with the specified title.
    6. numLong(): Creates a default long integer schema.
    
    Returns:
        A Schema object representing a long integer value.
    """
    
    # Static methods - numDouble
    numDouble = JavaMultipleMethod([
        ('(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Double;Ljava/lang/Double;)'
         'Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Double;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLjava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('()Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating double precision floating point schemas.
    
    These methods create Schema objects with type 'number' and format 'double' for double precision values.
    
    Creates a double precision floating point schema.
    
    Overloaded methods:
    1. numDouble(title, nullable, description, minimum, maximum): Creates a double schema with the 
       specified title, nullable flag, description, minimum value, and maximum value.
    2. numDouble(title, nullable, description, minimum): Creates a double schema with the specified 
       title, nullable flag, description, and minimum value.
    3. numDouble(title, nullable, description): Creates a double schema with the specified title, 
       nullable flag, and description.
    4. numDouble(title, nullable): Creates a double schema with the specified title and nullable flag.
    5. numDouble(title): Creates a double schema with the specified title.
    6. numDouble(): Creates a default double schema.
    
    Returns:
        A Schema object representing a double precision floating point value.
    """
    
    # Static methods - numFloat
    numFloat = JavaMultipleMethod([
        ('(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Double;Ljava/lang/Double;)'
         'Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Double;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLjava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('()Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating single precision floating point schemas.
    
    These methods create Schema objects with type 'number' and format 'float' for single precision values.
    
    Creates a single precision floating point schema.
    
    Overloaded methods:
    1. numFloat(title, nullable, description, minimum, maximum): Creates a float schema with the 
       specified title, nullable flag, description, minimum value, and maximum value.
    2. numFloat(title, nullable, description, minimum): Creates a float schema with the specified 
       title, nullable flag, description, and minimum value.
    3. numFloat(title, nullable, description): Creates a float schema with the specified title, 
       nullable flag, and description.
    4. numFloat(title, nullable): Creates a float schema with the specified title and nullable flag.
    5. numFloat(title): Creates a float schema with the specified title.
    6. numFloat(): Creates a default float schema.
    
    Returns:
        A Schema object representing a single precision floating point value.
    """
    
    # Static methods - str
    str = JavaMultipleMethod([
        ('(Ljava/lang/String;ZLcom/google/firebase/ai/type/StringFormat;Ljava/lang/String;)'
         'Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;ZLcom/google/firebase/ai/type/StringFormat;)Lcom/google/firebase/ai/type/Schema;',
         True, False),
        ('(Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('()Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating string schemas.
    
    These methods create Schema objects with type 'string' and various configurations.
    
    Creates a string schema.
    
    Overloaded methods:
    1. str(title, nullable, stringFormat, description): Creates a string schema with the specified 
       title, nullable flag, string format (e.g., 'date', 'email', 'uri'), and description.
    2. str(title, nullable, stringFormat): Creates a string schema with the specified title, 
       nullable flag, and string format.
    3. str(title, nullable): Creates a string schema with the specified title and nullable flag.
    4. str(title): Creates a string schema with the specified title.
    5. str(): Creates a default string schema.
    
    Returns:
        A Schema object representing a string value.
    """
    
    # Static methods - obj
    obj = JavaMultipleMethod([
        ('(Ljava/util/Map;Ljava/util/List;Ljava/lang/String;ZLjava/lang/String;)Lcom/google/firebase/ai/type/Schema;',
         True, False),
        ('(Ljava/util/Map;Ljava/util/List;Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/util/Map;Ljava/util/List;Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/util/Map;Ljava/util/List;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/util/Map;)Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating object schemas.
    
    These methods create Schema objects with type 'object' and various configurations.
    
    Creates an object schema.
    
    Overloaded methods:
    1. obj(properties, optional_properties, title, nullable, description): Creates an object schema with the 
       specified properties map, optional properties list, title, nullable flag, and description.
    2. obj(properties, optional_properties, title, nullable): Creates an object schema with the specified 
       properties map, optional properties list, title, and nullable flag.
    3. obj(properties, optional_properties, title): Creates an object schema with the specified properties map, 
       optional properties list, and title.
    4. obj(properties, optional_properties): Creates an object schema with the specified properties map and 
       optional properties list.
    5. obj(properties): Creates an object schema with the specified properties map.
    
    Parameters:
        properties: A map of property names to their corresponding Schema objects.
        required: A list of property names that are required in the object.
        title: The title of the schema.
        nullable: Whether the schema allows null values.
        description: A description of the schema.
    
    Returns:
        A Schema object representing an object with the specified properties.
    """
    
    # Static methods - array
    array = JavaMultipleMethod([
        ('(Lcom/google/firebase/ai/type/Schema;Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Integer;Ljava/lang'
         '/Integer;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Lcom/google/firebase/ai/type/Schema;Ljava/lang/String;ZLjava/lang/String;Ljava/lang/Integer;)Lcom/google'
         '/firebase/ai/type/Schema;', True, False),
        ('(Lcom/google/firebase/ai/type/Schema;Ljava/lang/String;ZLjava/lang/String;)Lcom/google/firebase/ai/type'
         '/Schema;', True, False),
        ('(Lcom/google/firebase/ai/type/Schema;Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Lcom/google/firebase/ai/type/Schema;Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Lcom/google/firebase/ai/type/Schema;)Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating array schemas.
    
    These methods create Schema objects with type 'array' and various configurations.
    
    Creates an array schema.
    
    Overloaded methods:
    1. array(items, title, nullable, description, minItems, maxItems): Creates an array schema with the 
       specified items schema, title, nullable flag, description, minimum items, and maximum items.
    2. array(items, title, nullable, description, minItems): Creates an array schema with the specified 
       items schema, title, nullable flag, description, and minimum items.
    3. array(items, title, nullable, description): Creates an array schema with the specified items 
       schema, title, nullable flag, and description.
    4. array(items, title, nullable): Creates an array schema with the specified items schema, title, 
       and nullable flag.
    5. array(items, title): Creates an array schema with the specified items schema and title.
    6. array(items): Creates an array schema with the specified items schema.
    
    Parameters:
        items: The Schema object that describes the items in the array.
        title: The title of the schema.
        nullable: Whether the schema allows null values.
        description: A description of the schema.
        minItems: The minimum number of items required in the array.
        maxItems: The maximum number of items allowed in the array.
    
    Returns:
        A Schema object representing an array with the specified configuration.
    """
    
    # Static methods - enumeration
    enumeration = JavaMultipleMethod([
        ('(Ljava/util/List;Ljava/lang/String;ZLjava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/util/List;Ljava/lang/String;Z)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/util/List;Ljava/lang/String;)Lcom/google/firebase/ai/type/Schema;', True, False),
        ('(Ljava/util/List;)Lcom/google/firebase/ai/type/Schema;', True, False)
    ])
    """
    Static factory methods for creating enumeration schemas.
    
    These methods create Schema objects with an 'enum' property that restricts values to a predefined set.
    
    Creates an enumeration schema.
    
    Overloaded methods:
    1. enumeration(values, title, nullable, description): Creates an enumeration schema with the 
       specified allowed values, title, nullable flag, and description.
    2. enumeration(values, title, nullable): Creates an enumeration schema with the specified 
       allowed values, title, and nullable flag.
    3. enumeration(values, title): Creates an enumeration schema with the specified allowed values 
       and title.
    4. enumeration(values): Creates an enumeration schema with the specified allowed values.
    
    Parameters:
        enum: A list of allowed values for the schema.
        title: The title of the schema.
        nullable: Whether the schema allows null values.
        description: A description of the schema.
    
    Returns:
        A Schema object representing an enumeration with the specified allowed values.
    """
    
    # Static methods - anyOf
    anyOf = JavaStaticMethod('(Ljava/util/List;)Lcom/google/firebase/ai/type/Schema;')
    """
    Static factory method for creating schemas that accept any of a list of schemas.
    
    This method creates a Schema object with an 'anyOf' property that allows data to conform
    to any one of the provided schemas.
    
    Creates a schema that accepts any of a list of schemas.
    
    Parameters:
        schemas: A list of Schema objects, any one of which the data may conform to.
    
    Returns:
        A Schema object representing a union type that accepts any of the specified schemas.
    """
