from unittest.mock import MagicMock
import pytest

from pytest_mock import mocker

import tweet

def test_main_when_tweet_exceeds_max_length(mocker):
    # Arrange
    tweet.MAX_TWEET_LEN = 0
    mock_tweet = "Mock tweet!"
    tweet.post_tweet = MagicMock()
    tweet.process_tweets = MagicMock()
    mocker.patch('tweet.load_and_concat', return_value=mock_tweet)
    # Act
    tweet.main(None)
    # Assert
    tweet.process_tweets.assert_called_once()
    
def test_process_tweets():
    # Arrange
    tweets = "This is a very long tweet. It has several characters more than the allowed length."
    tweet.MAX_TWEET_LEN = 50
    expected_result = ['This is a very long tweet. It has severa\n\n(1/3)', 'l characters more than the allowed lengt\n\n(2/3)', 'h.\n\n(3/3)']
    # Act
    result = tweet.process_tweets(tweets)
    # Asserts
    assert result == expected_result
