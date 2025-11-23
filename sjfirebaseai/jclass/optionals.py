from jnius import autoclass
from sjfirebaseai import package


RequestOptions = autoclass(f"{package}.type.RequestOptions")
