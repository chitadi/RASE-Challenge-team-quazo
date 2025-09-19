
# 🐳 Docker Setup Guide


This guide will help participants with **zero prior Docker experience** install and configure Docker on their system. Please contact us @ rase-challenge@ntu.edu.sg at anytime if you face any issues. 

---

## 1. Install Docker Engine

### Ubuntu / Debian (currently only supported guide)
```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Add Docker’s official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
# Add the Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 2. Verify installation
```bash
sudo docker --version
sudo docker run hello-world
```

## 3. Enable docker on boot
```bash
sudo systemctl enable docker
sudo systemctl start docker
```


## 4. Run without sudo, log out and log back in to take effect

By default, Docker requires `sudo` to run commands. To allow your user to run Docker without `sudo`, add yourself to the `docker` group:

```bash
# Create docker group if it doesn’t exist
sudo groupadd docker || true

# Add your user to the docker group
sudo usermod -aG docker $USER
```
⚠️ Log out and back in (or reboot) for changes to take effect.


## 5. Verify that docker has been fully setup and ready to run 
```bash
docker run hello-world
```

## 6. Congratulations, you have successfully installed docker!
Continue with running our prepared baseline docker in [#2. Running our baseline docker](../README.md#22-running-our-baseline-docker)

