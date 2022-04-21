#!/usr/bin/env bash

python evaluate.py \
    --user-dir ../../graphormer \
    --num-workers 16 \
    --dataset-name BBB_Martins \
    --user-data-dir ../../examples/customized_dataset \
    --task graph_prediction_with_flag \
    --arch graphormer_base \
    --num-classes 1 \
    --batch-size 64 \
    --save-dir ../../examples/tune_bbb/ckpts \
    --split test \
    --metric auc \
    --seed 1 \
    --pre-layernorm