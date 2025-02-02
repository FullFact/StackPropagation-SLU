# A Stack-Propagation Framework with Token-Level Intent Detection for Spoken Language Understanding

We want to automate the process of fact checking. We want our users to be able to search for a fact something like ‘has unemployment rise over the last two years?’. We then want to be able to understand the intent behind the question and return the relevant data.

An automated fact-checking system might include several different sub-tasks such as retrieving documents from a variety of sources that might either support or contradict a claim; detecting the stance of each article in regards to the purported claim; assessing the reputation and therefore the trustworthiness of each article; and claim verification, which evaluates both stance of the article and reputation of the source to establish how truthful the claim is.

Problem Breakdown:

- Understand user intent
- Find relevant information
- Use information to answer the question accurately
- Present the answer back to the user in a readable format




# Original Readme:
Token-Level Intent Detection for Spoken Language Understanding**. If you use any source codes or the datasets included in this toolkit in your work, please cite the following paper. The bibtex are listed below:

<pre>
@article{qin2019stack,
  title={A Stack-Propagation Framework with Token-Level Intent Detection for Spoken Language Understanding},
  author={Qin, Libo and Che, Wanxiang and Li, Yangming and Wen, Haoyang and Liu, Ting},
  journal={arXiv preprint arXiv:1909.02188},
  year={2019}
}
</pre>

In the following, we will guide you how to use this repository step by step.

## Architecture

<div align=center><img src="https://github.com/LeePleased/StackPropagation-SLU/blob/master/image/0.png" 
                   width="400" height="400" /></div>

## Preparation

Our code is based on PyTorch 1.1 and runnable for both windows and ubuntu server. Required python packages:
    
> + numpy==1.16.2
> + tqdm==4.32.2
> + scipy==1.2.1
> + torch==1.1.0
> + ordered-set==3.1.1

We highly suggest you using [Anaconda](https://www.anaconda.com) to manage your python environment.

## How to Run it

The script **train.py** acts as a main function to the project. For reproducing the results reported in our
paper, We suggest you the following hyper-parameter setting for ATIS dataset:

        python train.py -wed 256 -ehd 256 -aod 128 

Similarly, for SNIPS dataset, you can also consider the following command: 

        python train.py -wed 32 -ehd 256 -aod 128

Due to some stochastic factors, It's necessary to slightly tune the hyper-parameters using grid search. If you have any question, please issue the project or email [me](yangmingli@ir.hit.edu.cn) and we will reply you soon.
