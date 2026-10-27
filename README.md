# Road-Safety & Traffic-Law Assistant (Task 2: SFT + QLoRA)

A small LLM fine-tuned to answer Indian road-safety and Motor Vehicles Act questions.

## Problem definition
General models give generic or foreign answers (or refuse) on Indian traffic-law questions. Goal: a small, cheap model that answers in Indian terms (rupees, MV Act sections) and says "I am not sure" outside its knowledge.

## How to run
This needs an NVIDIA GPU, so run it in **Google Colab** (free T4):
1. Upload `train.ipynb` to colab.research.google.com.
2. Runtime > Change runtime type > **T4 GPU**.
3. (Optional, for the upload step) add a Colab secret `HF_TOKEN` with write access.
4. Runtime > Run all. The notebook clones the data from GitHub, or asks you to upload `road_safety.jsonl` and `heldout_test.jsonl`.

## Tech stack
| Item | Choice |
|---|---|
| Base model | Qwen2.5-1.5B-Instruct |
| Method | Supervised fine-tuning (SFT) with QLoRA, TRL `SFTTrainer` |
| Quantization | 4-bit NF4, double quantization, fp16 compute |
| LoRA | r=16, alpha=32, dropout 0.05, all attention and MLP projections |
| Training | 4 epochs, 64 steps, learning rate 2e-4, batch 2 x 4 accumulation |
| Compute | Google Colab, Tesla T4 (15 GB), about 158 s |
| Memory | about 3.8 GB GPU after training (`nvidia-smi`) |
| Adapter | https://huggingface.co/lisaluis717/road-safety-lora-1p5b |
| UI | Gradio chat in the last notebook cell |

## Dataset
- `road_safety.jsonl`: 122 chat-format training pairs. `heldout_test.jsonl`: 10 held-out pairs for honest testing.
- Built by `build_dataset.py` from Motor Vehicles (Amendment) Act 2019 penalty facts and the TOI editorial "Sense & Licence". Each fact is asked in several phrasings, plus "I am not sure, check the official source" examples for out-of-scope questions.
- Penalty amounts were written from memory and still need verification against the Act.

## Design principles
- **Honest evaluation:** held-out questions never appear in training; before/after comparison on the same questions.
- **Small and cheap:** 4-bit quantization plus LoRA trains on a free GPU.
- **Reduce made-up answers:** out-of-scope training examples teach the model to say it is not sure.
- **Reproducible:** one notebook, top to bottom, no secrets in it (token read from a Colab secret).

## Results
- **Before:** generic or refusing answers ("I can't provide information on this topic"), often in dollars.
- **After:** short answers with rupee amounts and section numbers; says "not sure" on out-of-scope questions.
- **Known failures:** it still mixes up some section numbers and statistics (for example the section for unlicensed driving, the 2015 death count, extra penalty details on helmets and repeat drink-driving). A 1.5B model with about 120 templated examples learns the format well but not every number. Fix: more varied pairs from real source text, with the section number in every answer.
- Screenshots: <!-- add screenshots here -->
