import json
import jsonschema
from jsonschema import validate
import sys
import os

def validate_agent_manifest(manifest_path, schema_path):
    try:
        # Load the manifest
        with open(manifest_path, 'r') as f:
            manifest_data = json.load(f)
        
        # Load the schema
        with open(schema_path, 'r') as f:
            schema_data = json.load(f)
        
        # Validate
        validate(instance=manifest_data, schema=schema_data)
        print(f"✅ Success: '{manifest_path}' is a valid Agent Manifest.")
        
    except FileNotFoundError as e:
        print(f"❌ Error: File not found - {e.filename}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Error: '{manifest_path}' is not a valid JSON file.")
        sys.exit(1)
    except jsonschema.exceptions.ValidationError as e:
        print(f"❌ Validation Error in '{manifest_path}':")
        print(f"   - Path: {'.'.join(map(str, e.path))}")
        print(f"   - Message: {e.message}")
        sys.exit(1)

if __name__ == "__main__":
    # Default paths
    SCHEMA = "docs/schemas/agent-manifest.schema.json"
    
    if len(sys.argv) < 2:
        print("Usage: python validate_manifest.py <path_to_your_manifest.json>")
        sys.exit(1)
        
    manifest_to_check = sys.argv[1]
    validate_agent_manifest(manifest_to_check, SCHEMA)
