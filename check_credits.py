import os
import json
from dotenv import load_dotenv
from edison_client import EdisonClient

def main():
    load_dotenv()
    api_key = os.getenv("EDISON_API_KEY")
    if not api_key:
        print("Error: API Key not found")
        return

    client = EdisonClient(api_key=api_key.strip())

    print("Fetching recent tasks...")
    # Get last 10 tasks to be safe
    tasks = client.get_tasks(limit=10)

    print(f"Found {len(tasks)} tasks.")
    
    total_cost = 0.0
    
    for task in tasks:
        # Inspect task for cost
        # The structure might be nested. 
        # Based on PQATaskResponse, cost might be in 'info.usage.total_cost' inside the environment state
        # But get_tasks returns a dict.
        
        t_id = task.get("id")
        t_query = task.get("task", "Unknown Query")
        
        # Try to find cost
        cost = 0.0
        
        # Check explicit cost field if any
        if "total_cost" in task:
             cost = task["total_cost"]
        
        # Check metadata or environment frame if available in get_tasks output
        # Usually get_tasks returns 'Lite' objects, might need to get full task details.
        
        print(f"Task: {t_query[:50]}... (ID: {t_id})")
        
        # If no cost here, we might need to fetch full task details for each
        # But let's see if we can find it in the dict first.
        # print(json.dumps(task, indent=2)) # Debugging
        
    print("-" * 30)
    print("Trying to fetch full details for recent tasks to find cost...")
    
    for task in tasks:
        t_id = task.get("id")
        try:
            full_task = client.get_task(t_id)
            # full_task is a TaskResponse object (or PQA/Phoenix subclass)
            
            this_cost = 0.0
            
            if hasattr(full_task, 'total_cost') and full_task.total_cost is not None:
                this_cost = full_task.total_cost
            
            print(f"Task {t_id}: Cost = ${this_cost:.4f} | Query: {full_task.query[:30]}...")
            total_cost += this_cost
            
        except Exception as e:
            print(f"Error fetching task {t_id}: {e}")

    print("=" * 30)
    print(f"Total Estimated Cost of Recent Tasks: ${total_cost:.4f}")

if __name__ == "__main__":
    main()
