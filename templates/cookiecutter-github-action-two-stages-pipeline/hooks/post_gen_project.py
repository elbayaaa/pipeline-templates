import os
from pathlib import Path

# move "pipeline.yaml" to the .github/workflow

Path('..', '.github', 'workflow').mkdir(parents=True, exist_ok=True)
os.rename("./pipeline.yaml", "../.github/workflow/pipeline.yaml")
