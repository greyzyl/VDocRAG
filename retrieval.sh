python -m vdocrag.vdocretriever.driver.search \
    --query_reps EMBEDDING_OUTPUT_DIR/query-sub500.pkl \
    --document_reps EMBEDDING_OUTPUT_DIR/corpus_sub5000.pkl  \
    --depth 1000 \
    --batch_size 64 \
    --save_text \
    --save_ranking_to EMBEDDING_OUTPUT_DIR/rank.txt \