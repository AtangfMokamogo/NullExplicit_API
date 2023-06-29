# NullExplicit API

## Project Description

NullExplicit API is a powerful API that provides two key functionalities for content moderation: NSFW image classification and sentiment analysis for text. This project aims to assist developers in building applications that require content filtering and moderation by providing reliable and efficient tools for analyzing and assessing the content's nature and sentiment.

## Key Features

- **NSFW Image Classification**: NullExplicit API offers an image classification endpoint specifically designed to detect and classify NSFW (Not Safe for Work) images. By utilizing advanced machine learning algorithms, the API can accurately identify explicit or inappropriate content, enabling developers to implement effective content filtering mechanisms.

- **Sentiment Analysis for Text**: The API provides a sentiment analysis endpoint that analyzes the sentiment expressed in a given piece of text. It can determine whether the text conveys a positive, negative, or neutral sentiment. This feature can be used to automatically moderate user-generated content or gain insights from large volumes of textual data.

- **Sentiment Analysis for Text**: The API provides an endpoint for creating a user account from a given username. This will return an Api-Key which can be used to access the other secured endpoints. 

## Installation

To access the NullExplicit API, you need to obtain an API key. Please follow the instructions on the NullExplicit API documentation website to register and obtain your API key. Once you have the API key, you can use it to authenticate your requests and access the endpoints.

## Endpoints

#### ```  BASE URL : ```  **Base URL: nullx.atangfino.tech/nullxapi/v1**

### NSFW Image Classification

## :exclamation: 

> The Image Recognition model used in implementing the NSFW classifier in this endpoint is in its `BETA` state. while care has been taken to filter out any incorrect results, the model will occasionally classify `nsfw` images as `safe` or `underwear`. The developer will like to apologize for any inconvinience the issue causes  

Endpoint: `/image_analysis`

**HTTP Method:** POST

**Request Parameters:**

- `image` (file): The image file to be classified.

**Response:**

The response contains the classification results for the provided image. It includes the probability scores for different categories, such as explicit, suggestive, or safe.

Example response:

```json
{
  "nsfw": 0.926,
  "safe": 0.074,
  "underwear": 0.0
}
```

## Sentiment Analysis for Text

Endpoint: `/text_analysis`

**HTTP Method:** POST

**Request Parameters:**

- `text` (string): The text to be analyzed for sentiment.

**Response:**

The response contains the sentiment analysis results for the provided text. It includes the sentiment label (positive, negative, or neutral) and the corresponding confidence score.

Example response:

```json
{
  "label": "positive",
  "confidence": 0.872
}
```
## User Creation

Endpoint: `/user`

**HTTP Method:** GET

**Request Parameters:**

- `username` (string): The desired username for the new user.

**Response:**

The response contains the API key for the newly created user.

Example response:

```json
{
  "apiKey": "e85bf624-3e02-4c28-a41c-44f6c6789d54"
}
```
## Usage

To utilize the NullExplicit API in your application, follow these steps:

1. Make sure you have obtained an API key from the NullExplicit API documentation website.

2. Include the API key in the headers or as a parameter when making API requests to authenticate your requests.

3. For NSFW image classification, send a POST request to the `/api/nsfw/classify` endpoint, providing the image file as the request payload. The API will respond with the classification results indicating the probability scores for different categories.

4. For sentiment analysis, send a POST request to the `/api/sentiment/analyze` endpoint, providing the text to be analyzed as the request payload. The API will respond with the sentiment analysis results, including the sentiment label and confidence score.

For detailed code examples and implementation instructions, please refer to the NullExplicit API documentation specific to your programming language.

## Contributing

Contributions to the NullExplicit API project are currently not accepted as the development is handled internally. However, feedback and suggestions are always welcome. If you have any ideas or encounter any issues, please contact us through the support channels mentioned below.

## License

NullExplicit API is released under the MIT License. Please review the terms and conditions of the license before using the API.

## Support

For any questions, issues, or assistance regarding the NullExplicit API, please reach out to our support channels mentioned below.

