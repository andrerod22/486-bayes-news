# Naive Bayes Fake News Detection

## Overview (Under Development Still)

The Naive Bayes Fake News Detection algorithm is a tool used for classifying news articles as either genuine or fake based on their textual content. This algorithm utilizes the principles of Naive Bayes classification, a probabilistic algorithm that assumes the independence of features, to make predictions about the authenticity of news articles.

## Importance

### Testing Reliability of News Sources

In today's digital age, the proliferation of fake news has become a significant concern, leading to misinformation and potential harm to individuals and society. The Naive Bayes Fake News Detection algorithm plays a crucial role in addressing this issue by providing a systematic approach to assessing the reliability of news sources. By analyzing the textual content of news articles and applying probabilistic reasoning, the algorithm can distinguish between trustworthy and untrustworthy sources, thereby helping users make informed decisions about the information they consume.

## Usage

### 1. Prepare Training Data

Gather a dataset of labeled news articles, with each article labeled as either genuine or fake. Ensure that the dataset represents a diverse range of sources and topics to improve the algorithm's performance.

### 2. Train the Algorithm

Run the `trainNaiveBayes` function to train the algorithm using the training data. This step involves calculating the probabilities of words appearing in genuine and fake news articles based on the provided dataset.

python
python train_naive_bayes.py labeled_news_dataset.txt

### 3. Test New Articles
Once the algorithm is trained, you can use it to classify new news articles as genuine or fake. Run the testNaiveBayes function to classify new articles based on their textual content.

### 4. Evaluaate Performance
Once the algorithm is trained, you can use it to classify new news articles as genuine or fake. Run the testNaiveBayes function to classify new articles based on their textual content.

## 5. Conclusion
The Naive Bayes Fake News Detection algorithm is a valuable tool for combating the spread of misinformation in the digital age. By leveraging probabilistic reasoning and linguistic analysis, the algorithm provides a reliable means of distinguishing between genuine and fake news articles, thereby empowering users to make informed decisions about the information they consume.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgements
The text preprocessing techniques used in this project are adapted from the first project see implementation at https://github.com/andrerod22/486-text-preprocessing 

## Contact
For any inquiries or questions, please contact andre.rodriguez9722@outlook.com