# Setup a remote or local cluster
Clone and follow the instructions in [this repo](https://github.com/IBM/it-bench-sample-scenarios/tree/main/sre). Setup a cluster, deploy the observability stack and a sample application, then inject a fault.

# Running with Docker/Podman
The agent should always be run in a container in order to prevent harmful commands being run on the user's PC.  

1. Clone the repo
```
git clone git@github.ibm.com:DistributedCloudResearch/lumyn.git
cd lumyn
```

2. Create a `.env` based on `.env.tmpl` by running:
```
cp .env.tmpl .env
```
Update the values here to switch LLM backends. Currently supported backends are watsonx.ai or Azure. Also update the values at the bottom so the agent can interact with your cluster. Remember that if you are using a local cluster you can access your PC http://localhost:3000 by using http://host.docker.internal:3000 (docker) or http://host.containers.internal:3000 (podman).

3. Build the image.
```
# Docker
docker build -t lumyn .
# Podman
podman build -t lumyn .
```

4. Run the image in interactive mode:
```
# Docker
docker run -it lumyn /bin/bash
# Podman
podman run -it lumyn /bin/bash
```
5. Start the agent:
```
crewai run
```

Pre-built images coming soon.

# Development Setup Instructions
1. Clone the repo
```
git clone git@github.ibm.com:DistributedCloudResearch/lumyn.git
cd lumyn
```

2. Ensure you have Python 3.12 installed. This project uses [uv](https://docs.astral.sh/uv/) for dependency management.
```
python -m venv crew_env

# Mac/Linux
source crew_env/bin/activate

# Windows
crew_env\Scripts\activate

pip install uv
pip install crewai==0.95.0
pip install crewai-tools
```
3. Navigate to the root project directory and install the dependencies using the CLI command:
```
crewai install
```
  
4. Create a `.env` based on `.env.tmpl` by running:
```
cp .env.tmpl .env
```
Update the values here to switch LLM backends.
  
5. Customize:  
- Modify `src/lumyn/config/agents.yaml` to define your agents
- Modify `src/lumyn/config/tasks.yaml` to define your tasks
- Modify `src/lumyn/crew.py` to add your own logic, tools and specific args
- Modify `src/lumyn/main.py` to add custom inputs for your agents and tasks
