#!/bin/bash

# Display usage if the type_model or the model_name/path is missing
if [ "$#" -ne 3 ]; then
    echo "Usage : $0 <out_path> <type_model> <model_name_or_path>"
    echo "  out_path         : Path to the output folder to save the results."
    echo "  type_model       : 'vllm' or 'hf'"
    echo "  model_name_or_path : HuggingFace model name or local path."
    exit 1
fi

# Get the args of the bash command line
if [ "$#" -eq 2 ]; then
    out_path="./results"
    type_model=$1
    m=$2
else
    out_path=$1
    type_model=$2
    m=$3
fi

# Create the output folder if necessary
mkdir -p "$out_path"

# Evaluation tasks from two domains : general and medical
GENERAL_TASKS=french_bench,include_base_44_french,global_mmlu_fr,mmlu_prox_fr,belebele_fra_Latn,mela_fr,mgsm_direct_fr,paws_fr,truthfulqa_fr_mc1,xwinograd_fr
MEDICAL_TASKS=glianorex_fr,clister,e3c-ner,medmcqafr,medqafr,medqafr5,mmlu_med_fr_anatomy,mmlu_med_fr_clinical_knowledge,mmlu_med_fr_college_biology,mmlu_med_fr_college_medicine,mmlu_med_fr_medical_genetics,mmlu_med_fr_professional_medicine,pubmedqafr

# Run lm-eval according to the model type
if [ "$type_model" == "vllm" ]; then
  lm_eval --model vllm --model_args pretrained=${m} --tasks $GENERAL_TASKS --output_path $out_path --device cuda:0 --log_samples
  lm_eval --model vllm --model_args pretrained=${m} --tasks $MEDICAL_TASKS --output_path $out_path --device cuda:0 --log_samples
elif [ "$type_model" == "hf" ]; then
  lm_eval --model hf --model_args pretrained=${m} --tasks $GENERAL_TASKS --output_path $out_path --device cuda:0 --log_samples --batch_size auto
  lm_eval --model hf --model_args pretrained=${m} --tasks $MEDICAL_TASKS --output_path $out_path --device cuda:0 --log_samples --batch_size auto
else
  echo "Le type de modèle doit être 'vllm' ou 'hf'"
  exit 1
fi
