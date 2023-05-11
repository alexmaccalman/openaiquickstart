# Superhero Animal Names Generator

The Superhero Animal Names Generator is a web application that suggests superhero names for different animals. It uses OpenAI's text-based language model to generate creative and fun names for animals based on their species.

## How It Works

1. The user selects an animal from the provided list.
2. The application sends a request to the server with the selected animal.
3. The server uses OpenAI's Completion API to generate three superhero names for the selected animal.
4. The server responds with the generated names.
5. The web page displays the suggested names for the user to see and enjoy.

## Technologies Used

- Python: The server-side logic is written in Python, which handles the user requests and communicates with OpenAI's API.
- Flask: The web framework used to build the application and handle HTTP requests.
- OpenAI API: The application leverages OpenAI's Completion API to generate the superhero names for the animals.
- HTML/CSS: The front-end interface of the application is built using HTML and CSS.
- Azure Container Instance: The application can be deployed as a containerized application using Azure Container Instance.

## Prerequisites

Before running the application, make sure you have the following:

- OpenAI API key: You need to sign up for OpenAI and obtain an API key. This key is used to authenticate requests to the OpenAI API.
- Python installed: Make sure you have Python installed on your machine.

## Getting Started

1. Clone this repository: `git clone <repository-url>`
2. Install the required Python packages: `pip install -r requirements.txt`
3. Set your OpenAI API key as an environment variable:
   - For Linux/macOS: `export OPENAI_API_KEY=<your-api-key>`
   - For Windows: `set OPENAI_API_KEY=<your-api-key>`
4. Run the application: `python app.py`
5. Open your web browser and go to `http://localhost:5000` to access the Superhero Animal Names Generator.

## Deployment to Azure Container Instance

To deploy the application to Azure Container Instance, follow these steps:

1. Build the container image: `docker build -t superhero-animal-names .`
2. Push the container image to a container registry: `docker push <registry-name>/superhero-animal-names`
3. Update the `<your-registry-info>` placeholders in the `azure-deploy.sh` script with your container registry information.
4. Run the deployment script: `./azure-deploy.sh`

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
