import json
import pytest
from pathlib import Path
from pydantic import ValidationError
from operations.models.pipeline_data import TestPipeline, PipelineCollection

def load_pipelines():
    pipeline_dir = Path(__file__).parent.parent / "data"
    all_pipelines = []
    
    for file_path in pipeline_dir.glob("*.json"):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                
                if "pipelines" in data and isinstance(data["pipelines"], list):
                    collection = PipelineCollection.model_validate(data)
                    for pipeline in collection.pipelines:
                        all_pipelines.append(_process_pipeline(pipeline))
                else:
                    pipeline = TestPipeline.model_validate(data)
                    all_pipelines.append(_process_pipeline(pipeline))

            except json.JSONDecodeError:
                print(f"Warning: Could not decode JSON from {file_path.name}")
            except ValidationError as e:
                print(f"\nValidation Error in {file_path.name}:\n{e}")
            except Exception as e:
                print(f"Warning: Error processing {file_path.name}. Error: {e}")
                
    return all_pipelines

def _process_pipeline(pipeline: TestPipeline) -> pytest.param:
    """Helper to process a single TestPipeline model."""
    markers = [getattr(pytest.mark, m) for m in pipeline.markers if hasattr(pytest.mark, m)]
    return pytest.param(
        pipeline,
        id=pipeline.test_id,
        marks=markers
    )