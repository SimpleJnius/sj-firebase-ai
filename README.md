# SJ-Firebase-AI - Gemini API using Firebase AI Logic

Build AI-powered mobile apps and features with the Gemini and Imagen models using Firebase AI Logic
through SimpleJnius python bridge

Firebase AI Logic gives you access to the latest generative AI models from Google: the Gemini models
and Imagen models.

If you need to call the Gemini API or Imagen API directly from your mobile app 
— rather than server-side — you can use the Firebase AI Logic client SDKs. These client SDKs are built
specifically for use with mobile apps, offering security options against unauthorized clients
as well as integrations with other Firebase services.

Need more flexibility or server-side integration?
[Genkit](https://genkit.dev/) is Firebase's open-source framework for sophisticated server-side AI
development with broad access to models from Google, OpenAI, Anthropic, and more. It includes more
advanced AI features and dedicated local tooling.

Read more for [here](https://firebase.google.com/docs/ai-logic#key-capabilities) for key capabilities
and other important information


## Get started with the Gemini API using the Firebase AI Logic SDKs through SimpleJnius python bridge

This guide shows you how to get started making calls to the Gemini API directly from your app using 
the Firebase AI Logic client SDKs for your chosen platform.

### Step 1: Set up a Firebase project and connect your app

1. Sign into the [Firebase console](https://console.firebase.google.com), and then select your Firebase project.

   **Don’t already have a Firebase project?**

   If you don’t already have a Firebase project, click the button to create a new Firebase project, and then use either of the following options:

   - **Option 1:** Create a wholly new Firebase project (and its underlying Google Cloud project automatically) by entering a new project name in the first step of the workflow.

   - **Option 2:** “Add Firebase” to an existing Google Cloud project by clicking **Add Firebase to Google Cloud project** (at bottom of page).  
     In the first step of the workflow, start entering the **project name** of the existing project, and then select the project from the displayed list.

   Complete the remaining steps of the on-screen workflow to create a Firebase project.  
   **Note:** When prompted, you do **not** need to set up Google Analytics to use the Firebase AI Logic SDKs.

2. In the Firebase console, go to the [**Firebase AI Logic** page](https://console.firebase.google.com/project/_/ailogic?_gl=1*2eotce*_ga*ODAyMTIxNjk3LjE3NjA2MDUxMzg.*_ga_CW55HF8NVT*czE3NjU4MDk3MzMkbzExNSRnMSR0MTc2NTgxMjQwMiRqNjAkbDAkaDA.).

3. Click **Get started** to launch a guided workflow that helps you set up the **[required APIs](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#required-apis) and resources** for your project.

4. Select the **Gemini API** provider that you’d like to use with the Firebase AI Logic SDKs.  
   *Gemini Developer API is recommended for first-time users.*  
   You can always add billing or set up Vertex AI Gemini API later, if you’d like.

   - **Gemini Developer API** — *billing optional*  
     (available on the no-cost Spark pricing plan, and you can upgrade later if desired)

     The console will enable the required APIs and create a Gemini API key in your project.  
     **Do not add this Gemini API key into your app’s codebase.**  
     [Learn more](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#add-gemini-api-key-to-codebase)

   - **Vertex AI Gemini API** — *billing required*  
     (requires the pay-as-you-go Blaze pricing plan)

     The console will help you set up billing and enable the required APIs in your project.

5. If prompted in the console’s workflow, follow the on-screen instructions to register your app and connect it to Firebase.

6. Continue to the next step in this guide to add the SDK to your app.

### Step 2: Add the SDK

With your Firebase project set up and your app connected to Firebase (see previous step),
you can now add the Firebase AI Logic SDK to your app.

In your `buildozer.spec` file, add the following dependencies
```spec
requirements = ... other python dependencies, sjfirebaseai, simplejnius
android.gradle_dependencies = ... other android dependencies,com.google.firebase:firebase-ai,
   com.google.guava:guava:31.0.1-android,org.reactivestreams:reactive-streams:1.0.4
p4a.fork = simplejnius
p4a.branch = firebase
```

### Step 3: Initialize the service and create a model instance
```python
from sjfirebaseai.jclass import (
    FirebaseAI,
    GenerativeModelFutures,
    GenerativeBackend
)


# Initialize the Gemini Developer API backend service
# Create a `GenerativeModel` instance with a model that supports your use case
ai = FirebaseAI.getInstance(GenerativeBackend.vertexAI())  # or GenerativeBackend.googleAI()

# Use the GenerativeModelFutures Java compatibility layer which offers
# support for ListenableFuture and Publisher APIs
model = GenerativeModelFutures.from_(ai)
```

Note that **depending on the capability you're using, you might not always create a GenerativeModel instance.**

- To [access an Imagen model](https://firebase.google.com/docs/ai-logic/generate-images-imagen),
create an ImagenModel instance.
- To [stream input and output using the Gemini Live API](https://firebase.google.com/docs/ai-logic/live-api),
create a LiveModel instance.

Also, after you finish this getting started guide, learn how to choose a
[model](https://firebase.google.com/docs/ai-logic/models) for your use case and app.

> [!IMPORTANT]
> Before going to production, we strongly recommend implementing Firebase Remote Config so that you can
> [remotely change the model name used in your app](https://firebase.google.com/docs/ai-logic/change-model-name-remotely).

### Step 4: Send a prompt request to a model

```python
from sjfirebaseai.jclass import (
    FirebaseAI,
    GenerativeModelFutures,
    GenerativeBackend,
    Content
)
from simplejnius.guava.jinterface import FutureCallback
from simplejnius.guava.jclass import Futures


# Initialize the Gemini Developer API backend service
# Create a `GenerativeModel` instance with a model that supports your use case
ai = FirebaseAI.getInstance(GenerativeBackend.vertexAI())  # or GenerativeBackend.googleAI()

# Use the GenerativeModelFutures Java compatibility layer which offers
# support for ListenableFuture and Publisher APIs
model = GenerativeModelFutures.from_(ai)

# Provide a prompt that contains text
prompt = (
    Content.Builder()
    .addText("Write a story about a Kivy Framework.")
    .build()
)

# To generate text output, call generateContent with the text input
response = model.generateContent(prompt)

def on_success(result):
    print(result.getText())
    
def on_failure(error):
    print(error.getLocalizedMessage())

# To avoid garbage collection, make sure the FutureCallback instance is not stored in a 
# function scope variable
future_callback = FutureCallback(on_success, on_failure)
Futures.addCallback(response, future_callback)
```

### Stream the response

```python
from sjfirebaseai.jclass import (
    FirebaseAI,
    GenerativeModelFutures,
    GenerativeBackend,
    Content
)
from simplejnius.reactivestreams.jinterface import Subscriber


# Initialize the Gemini Developer API backend service
# Create a `GenerativeModel` instance with a model that supports your use case
ai = FirebaseAI.getInstance(GenerativeBackend.vertexAI())  # or GenerativeBackend.googleAI()

# Use the GenerativeModelFutures Java compatibility layer which offers
# support for ListenableFuture and Publisher APIs
model = GenerativeModelFutures.from_(ai)

# Provide a prompt that contains text
prompt = (
    Content.Builder()
    .addText("Write a story about a Kivy Framework.")
    .build()
)

# To stream generated text output, call generateContentStream with the text input
streaming_response = model.generateContentStream(prompt)

# Subscribe to partial results from the response
full_response = ""

def on_next(generate_content_response):
    global full_response
    chunk = generate_content_response.getText()
    full_response += chunk

# To avoid garbage collection, make sure the Subscriber instance is not stored in a 
# function scope variable
subscriber = Subscriber(
    {
        "on_next": on_next,
        "on_complete": lambda: print(full_response),
        "on_error": lambda error: None,
        "on_subscribe": lambda sub: None
    }
)
streaming_response.subscribe(subscriber)
```