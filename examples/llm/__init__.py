# Copyright 2022 MosaicML Examples authors
# SPDX-License-Identifier: Apache-2.0

try:
    import torch

    from examples.llm.src.flash_attention import FlashAttention, FlashMHA
    if torch.cuda.is_available():
        from examples.llm.src.flash_attn_triton import \
            flash_attn_func as flash_attn_func_llm # type: ignore
        from examples.llm.src.flash_attn_triton import \
            flash_attn_qkvpacked_func as flash_attn_qkvpacked_func_llm # type: ignore
    from examples.llm.src.hf_causal_lm import ComposerHFCausalLM
    from examples.llm.src.model_registry import COMPOSER_MODEL_REGISTRY
    from examples.llm.src.mosaic_gpt import (GPTMLP, ComposerMosaicGPT,
                                             FlashCausalAttention, GPTBlock,
                                             MosaicGPT, TorchCausalAttention,
                                             TritonFlashCausalAttention,
                                             alibi_bias)
    from examples.llm.src.tokenizer import (TOKENIZER_REGISTRY, HFTokenizer,
                                            LLMTokenizer)
except ImportError as e:
    try:
        is_cuda_available = torch.cuda.is_available()  # type: ignore
    except:
        is_cuda_available = False

    extras = '.[llm]' if is_cuda_available else '.[llm-cpu]'
    raise ImportError(
        f'Please make sure to pip install {extras} to get the requirements for the LLM example.'
    ) from e

__all__ = [
    'FlashAttention',
    'FlashMHA',
    'ComposerHFCausalLM',
    'COMPOSER_MODEL_REGISTRY',
    'TorchCausalAttention',
    'FlashCausalAttention',
    'TritonFlashCausalAttention',
    'alibi_bias',
    'GPTMLP',
    'GPTBlock',
    'MosaicGPT',
    'ComposerMosaicGPT',
    'LLMTokenizer',
    'HFTokenizer',
    'TOKENIZER_REGISTRY',

    # These are commented out because they only exist if CUDA is available
    # 'flash_attn_func_llm',
    # 'flash_attn_qkvpacked_func_llm'
]
