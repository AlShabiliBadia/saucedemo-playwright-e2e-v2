from pydantic import BaseModel
from typing import List, Annotated
from typing_extensions import Annotated
from .__init__ import Operation, Field

class TestPipeline(BaseModel):
    test_id: Annotated[str, Field(min_length=1)]
    markers: List[str] = []
    operations: List[Operation]

class PipelineCollection(BaseModel):
    pipelines: List[TestPipeline]