# Instructions to participants

Please contact us @ rase-challenge@ntu.edu.sg at anytime if you face any issues during the course of this set-up. 

# Download
Download the baseline and training code from this repo. 

```
git clone RASE-challenge/challenge_baseline2026
```

and link dataset from your email after you have registered.


After downloading, unzip the dataset.zip into the repo, and check that the file directory is as such:
```text
challenge_baseline2026/
├── dataset/ # unzip the downloaded dataset and copy into this directory
│   ├── Task1/
│   └── Task2/
├── results/
├── src/
│   ├── config/ 
│   ├── logs/  
│   ├── metrics/ 
│   ├── models/
│   ├── train.py        
│   ├── datamodule.py
│   ├── save_for_submission.py
│   └── utils.py
├── baseline_docker_build.sh
├── baseline_docker_run.sh
├── baseline.dockerfile
├── docker_submission.sh
├── full_submission.sh
├── config.sh
└── README.md
```


## 1. Installing docker on your system

Please follow the quick-start [docker guide](docs/docker_setup_ubuntu.md) that is aimed to help participants with **zero prior Docker experience** install and configure Docker on their system. 


## 2. Running our baseline docker
We have prepared a docker baseline for you to extend (we have prepared a guide for that too). Please make sure that the docker is installed, with [running without sudo enabled](docs/docker_setup_ubuntu.md#4-run-without-sudo-log-out-and-log-back-in-to-take-effect).

Run the build command in challenge_baseline folder via
```bash 
bash baseline_docker_build.sh
```
Followed by the run command
```bash 
bash baseline_docker_run.sh
```

Once successful, you should see 
```bash
root@<container_id>:/src#
```

## 3. VS code set-up (optional)
We recommend using **Visual Studio Code (VS Code)** as your main editor.  
It’s lightweight, cross-platform, and works well with both Python and Docker.
Follow our [VS Code Setup Guide for docker](./docs/vscode_setup.md) (optional).

## 4. Run the training code in the container

Note: Make sure that your command prompt is in root@<container_id>.

Run the following command to train. Note that there are three phases, first with `fast development run` (fast_dev_run), second with `full training`  and finally with `full validation run`.
```bash
bash train.py
```
The rationale for the fast dev run phase is to facilitate quick fails (i.e., code issues, etc).  For now, you can terminate the training script (via `Ctrl+C`) after it has completed the fast development run phase and leverage it's saved file to test the submission portal.

## 5. Submit a dummy evaluation result (in progress, will be released on 27th)


## 6. Innovate your new model!
The code base is prepared to allow easy extension. To make your new model, copy the baseline model and configuration made in the following folders/files:
```text
challenge_baseline/
├── src/
│   ├── config/train_baseline.yaml  <- copy this and paste
│   ├── models/WaveVoiceNet.py <- copy this and paste        
│   ├── train.py        
│   ├── datamodule.py
│   └── utils.py
├── baseline_docker_build.sh
├── baseline_docker_run.sh
├── baseline.dockerfile
├── config.sh
└── README.md
```

Then 




