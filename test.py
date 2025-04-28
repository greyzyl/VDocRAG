from datasets import load_dataset
train_data = load_dataset(
    "/home/zhuyinglian/fdu02_dir/zyl/downloads/QA_data_sub5000",
    None,
    data_files=None,
    split='train',
    cache_dir=None,
)
corpus  = load_dataset(
                '/home/zhuyinglian/fdu02_dir/zyl/downloads/corpus_data_sub5000',
                None,
                data_files=None,
                split='train',
                cache_dir=None,
)
print(train_data[0])
print(corpus[0])