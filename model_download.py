from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("9b2a518bb3b74d8db0c252c25acd4368", path="model")
print(f"Placed model in: {my_model}")