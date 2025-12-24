# Edison Client Usage Guide

This guide explains how to install and use the **Edison Client** to access the Edison Scientific platform's AI capabilities.

## 1. Overview
The Edison Client (`edison-client`) is a Python library that allows you to interact with Edison Scientific's platform. You can submit various types of scientific tasks (jobs) such as literature searches, data analysis, and chemistry tasks.

## 2. Prerequisites
- **Python**: Ensure you have Python installed.
- **API Key**: You need an API key from your [Edison Platform Profile](https://platform.edisonscientific.com/profile).

## 3. Installation
You can install the client using `pip` (or `uv` if you use it).

```bash
pip install edison-client
```
*Note: The official docs mention `uv pip install edison-client`.*

## 4. Basic Usage

### Initialize the Client
First, import the client and initialize it with your API key.

```python
from edison_client import EdisonClient, JobNames

# Replace with your actual API key
client = EdisonClient(api_key="your_api_key_here")
```

### Running a Task
To run a task, define a dictionary with the job `name` and your `query`.

```python
# specific job types are available in JobNames enum
task_data = {
    "name": JobNames.LITERATURE,
    "query": "Which neglected diseases had a treatment developed by artificial intelligence?",
}

# Run synchronously (blocks until done)
task_response = client.run_tasks_until_done(task_data)

print(task_response.answer)
```

## 5. Available Job Types (JobNames)
You can choose different agents for different tasks:

| Job Name | Description | Use Case |
| :--- | :--- | :--- |
| `JobNames.LITERATURE` | Literature Search (PaperQA3) | Scientific questions requiring cited responses. |
| `JobNames.PRECEDENT` | Precedent Search (HasAnyone) | Checking if an experiment or idea has been done before. |
| `JobNames.MOLECULES` | Chemistry Tasks (Phoenix) | Synthesis planning, molecule design, cheminformatics. |
| `JobNames.ANALYSIS` | Data Analysis | Analyzing biological datasets. |
| `JobNames.DUMMY` | Dummy Task | Testing connection and setup. |

## 6. Advanced Features

### Asynchronous Execution
For long-running tasks or integration into async applications:

```python
import asyncio

async def main():
    task_response = await client.arun_tasks_until_done(task_data)
    print(task_response.answer)

asyncio.run(main())
```

### Batch Processing
You can submit a list of tasks at once:

```python
tasks = [
    {"name": JobNames.PRECEDENT, "query": "Query 1..."},
    {"name": JobNames.LITERATURE, "query": "Query 2..."}
]
responses = client.run_tasks_until_done(tasks)
for resp in responses:
    print(resp.answer)
```

## 7. Resources
- [Official Documentation](https://edisonscientific.gitbook.io/edison-cookbook/edison-client)
