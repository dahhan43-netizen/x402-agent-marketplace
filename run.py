"""Run the agent marketplace server."""
import uvicorn
import sys
from pathlib import Path

# Add the marketplace directory to path
marketplace_dir = Path(__file__).parent
sys.path.insert(0, str(marketplace_dir))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
