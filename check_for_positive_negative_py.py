{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "check_for_positive_negative.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMf6fFpjoU5zLmMRcrp88Ov",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ritikkumar01111999/Fake-Job-Posting-Prediction/blob/master/check_for_positive_negative_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vN7ZcOEPGRs-",
        "outputId": "0d694f82-568d-4d5a-a8f0-bf5e20905f0a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter here your number:-25\n",
            "number is possitive\n",
            "None\n"
          ]
        }
      ],
      "source": [
        "#check the number if it in possitive negative or zero\n",
        "def check(a):\n",
        "  if a>0:\n",
        "    print('number is possitive')\n",
        "  if a<0:\n",
        "    print('the number is negative')\n",
        "  if a==0:\n",
        "    print('number is zero')\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  \n",
        "  a=int(input('enter here your number:-'))\n",
        "  print(check(a))\n"
      ]
    }
  ]
}