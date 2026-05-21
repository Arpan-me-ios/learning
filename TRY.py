from google.cloud import aiplatform

aiplatform.init(project="gen-lang-client-0134822810", location="asia-southeast1")

models = aiplatform.Model.list()
for model in models:
    print(model.resource_name, model.display_name)