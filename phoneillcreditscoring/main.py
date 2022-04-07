import apache_beam as beam
from apache_beam.options.pipeline_options import (StandardOptions)
import os
from .pardos.mypardo import MyPardo

pipeline_options = PipelineOptions(
        streaming=streaming, save_main_session=True,
        setup_file=os.path.join(os.path.dirname(__file__), "..", "setup.py"),
requirements_file=os.path.join(os.path.dirname(__file__), "..", "requirements.txt"),
)

def run():
  p = beam.Pipeline(options=pipeline_options):
  p | beam.io.ReadFromPubSub(topic=topic) | beam.ParDo(MyPardo())

  pipeline_result = p.run()

  # Used while testing locally
  if pipeline_options.view_as(StandardOptions).runner == "DirectRunner":
    pipeline_result.wait_until_finish()
