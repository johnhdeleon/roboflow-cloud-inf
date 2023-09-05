# Real-time Object Detection with Roboflow on cloud and your Webcam

Perform real-time object detection using your Roboflow custom model and OpenCV. This project connects to a Roboflow project, retrieves a model, and uses it to make live object detection inferences using your webcam.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed
- Roboflow API key (You can obtain one from Roboflow)
- OpenCV and supervision Python libraries (You can install them via `pip`)

## Installation

1. Clone this repository:

```shell
  git clone https://github.com/johnhdeleon/roboflow-cloud-inf.git
  cd roboflow-cloud-inf
```

2. Install the required libraries using the provided requirements.txt file:

```shell
pip install -r requirements.txt
```
If you are already using these libraries or need different versions you can create a new environment using virtualenv 
or with python -m venv myenv where myenv is the name of your environment

3. Update the code with your Roboflow API Key and project details:

```shell
# Specify your Roboflow API Key
rf = Roboflow(api_key="YOUR_API_KEY")

# Specify your Roboflow project name
project = rf.workspace().project("YOUR_PROJECT_NAME")

# Specify your Roboflow project version
model = project.version(YOUR_MODEL_VERSION).model
```
4. Run the script:

```shell
python app.py
```
## Usage

- Adjust the confidence and overlap parameters in the model.predict method for your specific use case.
- Press the 'q' key to exit the real-time detection window.



