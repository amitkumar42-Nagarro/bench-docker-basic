# Docker / Docker Compose Command Demostration

## How to setup and run
### Install Dcoker and Docker compose
> - *sudo groupadd docker*
> - *sudo usermod -aG docker ${USER}*
> - *curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
> - *sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"*
> - *sudo apt-get update*
> - *sudo apt-get install -y docker-ce containerd.io*
> - *echo "sudo service docker start" >> ~/.profile*

### Run docker build images
> - *docker compose build .  --no-cache*

### Run docker up to start conrainer
> - *docker compose up -d*

### validate in browser FRONTEND (based on configured port 3000)
> - *http://localhost:3000/*

### validate in browser BACKEND APIs (based on configured port 5001)
> - *http://localhost:5001/*
> - *http://localhost:5001/tasks*

### to stop both containers including network
> - *docker compose down*

<br></br>
## List of command with details [COMMANDS LIST](commands\commands.md)


