model_cfg = {
    'word_level': True,  # set to True if want to train a word-level model (requires more data and smaller max_length)
    'rnn_size': 128,  # number of LSTM cells of each layer (128/256 recommended)
    'rnn_layers': 2,  # number of LSTM layers (>=2 recommended)
    'rnn_bidirectional': False,  # consider text both forwards and backward, can give a training boost
    'max_length': 8,
    # number of tokens to consider before predicting the next (20-40 for characters, 5-10 for words recommended)
    'max_words': 100000,  # maximum number of words to model; the rest will be ignored (word-level model only)
}

train_cfg = {
    'line_delimited': True,  # set to True if each text has its own line in the source file
    'num_epochs': 5,  # set higher to train the model for longer
    'gen_epochs': 1,  # generates sample text from model after given number of epochs
    'train_size': 0.8,  # proportion of input data to train on: setting < 1.0 limits model from learning perfectly
    'dropout': 0.0,  # ignore a random proportion of source tokens each epoch, allowing model to generalize better
    'validation': False,  # If train__size < 1.0, test on holdout dataset; will make overall training slower
    'is_csv': False  # set to True if file is a CSV exported from Excel/BigQuery/pandas
}

file_name = "marathon_terminals.txt"
model_name = "marathon_terminal"
