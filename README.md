# Instructions to participants

Please contact us @ rase-challenge@ntu.edu.sg at anytime if you face any issues during the course of this set-up. 

# Download
Download the baseline and training code from this repo. 

```
git clone rase_challenge/challenge_baseline2026
```


and dataset from your email after you have registered.

Make sure you have 
, run 



After downloading, 
  which should contain these file directory:
```text
challenge_baseline/
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

## 5. Submit a dummy evaluation result (in progress)

To facilitate the submission during the testing phase, we have prepared some trial examples for submitting. Our team believe in protecting your hard work in this challenge and hence, provided a way to protect your IP.

In the following, we outline the submission which will need two files: 
- A zip file for checkpoint, source code, configuration, etc
- A requirement file for python installation and apt-get installed software for docker (if installation, etc. has been made to the provided base docker)

For the first file, in your docker terminal, run the following command to store the checkpoint, source code, and configuration via
```python
python3 save_for_submission.py -c <best_model_yaml>
```
where `<best_model_yaml>` indicates the configuration file to the best model for testing. The configuration file can be found after the `train.py` script is ran.

For this example, you will run with a provided configuration file via
```python
# in the docker
python3 save_for_submission.py -c /results/WaveVoiceNet__learning_rate=0.001_fast_dev_run/fast_dev_run.yaml
```
and it will generate a zip file:
```text 
/results/WaveVoiceNet__learning_rate=0.001_fast_dev_run/model_submission.zip
```

Note the directory of this zip file, which is needed for the final bundle.

For the second file (optional if you need to install more packages), perform the following (using the example config):
```bash
# in the docker terminal
pip install cowpy # e.g.   

# on the host terminal
docker commit rase2026-baseline rase2026:v0.0 # save as a new image
docker save -o docker_submission.tar rase2026:baseline rase2026:v0.0 
``` 

With the above, you should have the following files:
```text
challenge_baseline/
├── results/
│   └── WaveVoiceNet__learning_rate=0.001_fast_dev_run
│       └──model_submission.zip
├── src/
│   └── ...
├── ...
├── docker_submission.tar
└── full_submission.sh
```

For the final bundle run the following:
```bash
# on the host terminal
cd challenge_baseline/
bash full_submission.sh -m=<.../model_submission.zip> -d=<.../docker_submission.tar>
```

For our example, it will be shown as 
```bash
# on the host terminal
cd challenge_baseline/
bash full_submission.sh -m=./results/WaveVoiceNet__learning_rate=0.001_fast_dev_run/model_submission.zip -d=./docker_submission.tar
```

Note that if you do not have new package on docker, 
```bash
# on the host terminal
cd challenge_baseline/
bash full_submission.sh -m=./results/WaveVoiceNet__learning_rate=0.001_fast_dev_run/model_submission.zip 
```

Once the full bundle is completed, upload the full_submission.zip to EvalAI!


## 6. Innovate your new model!
The code base is prepared to allow easy extension. To make your new model, copy can be made in the following folders/files:
```text
challenge_baseline/
├── src/
│   ├── config/train_baseline.yaml  
│   ├── models/WaveVoiceNet.py         
│   ├── train.py        
│   ├── datamodule.py
│   └── utils.py
├── baseline_docker_build.sh
├── baseline_docker_run.sh
├── baseline.dockerfile
├── config.sh
└── README.md
```





