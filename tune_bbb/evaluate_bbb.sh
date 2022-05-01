#!/usr/bin/env bash

python evaluate.py \
    --user-dir ../../graphormer \
    --num-workers 16 \
    --dataset-name BBB_Martins_Random \
    --user-data-dir ../../examples/customized_dataset \
    --task graph_prediction_with_flag \
    --arch graphormer_base \
    --num-classes 1 \
    --batch-size 64 \
    --save-dir /n/data1/hms/dbmi/zitnik/lab/users/an252/BBB/ckpts/2022.04.30_2 \
    --split test \
    --metric auc \
    --seed 1 \
    --pre-layernorm
