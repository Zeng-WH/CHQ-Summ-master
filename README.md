# Reinforcement Learning for Abstractive Question Summarization with Question-aware Semantic Rewards



The code requires **Python 3** and please install the Python dependencies with the command:
```bash
pip install -r requirements.txt
```

The original MeQSum dataset is available [here](https://github.com/abachaa/MeQSum).


### Running the code 
1. Please make sure to download the pre-trained question-type identification and question-focus recognition models from [here](https://drive.google.com/drive/folders/1ePtuMPR20rZSgZbarSnno4-sqazLJVn0?usp=sharing) and 
    place it in the current directory.

2. Fine tune ProphetNet model on MeQSum dataset

    Follow the instrcution from transformers repo.
    https://github.com/huggingface/transformers/tree/v4.1.1/examples/seq2seq
 

3. Train MLE + RL Model
    ```
    python main.py --train_mode rl --trained_model_path /path/to/the/fine-tuned/prophetnet/model
    ```

4. Test Model
    ```
    python main.py --model test --trained_model_path /path/to/the/saved/model

    ```


## Reference

If you are using this code for your reseach work then please cite our paper:
```
@inproceedings{yadav-etal-2021-reinforcement,
    title = "Reinforcement Learning for Abstractive Question Summarization with Question-aware Semantic Rewards",
    author = "Yadav, Shweta  and
      Gupta, Deepak  and
      Ben Abacha, Asma  and
      Demner-Fushman, Dina",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-short.33",
    doi = "10.18653/v1/2021.acl-short.33",
    pages = "249--255"
    }
```
