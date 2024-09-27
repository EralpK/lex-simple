## install easse and readability packages

from easse.sari import corpus_sari
from easse.fkgl import corpus_fkgl
import numpy as np
import pandas as pd

from readability import Readability

input_file_og = open("raw_data/supreme_org_test.txt","r").read().strip().split('\n')
ref_file1_og = open("raw_data/supreme_test_labels1.txt","r").read().strip().split('\n')
ref_file2_og = open("raw_data/supreme_test_labels2.txt","r").read().strip().split('\n')
ref_file3_og = open("raw_data/supreme_test_labels3.txt","r").read().strip().split('\n')
uslt_noss_wo_bert_og = open("files/uslt_noss_wo_bert_supreme_test.txt","r").read().strip().split('\n') #37.470484
uslt_noss_wo_lm_loss_og = open("files/uslt_noss_wo_lm_loss_supreme_test.txt","r").read().strip().split('\n') #37.470484
uslt_noss_wo_cos_sim_og = open("files/uslt_noss_wo_cos_sim_supreme_test.txt","r").read().strip().split('\n') #37.470484
uslt_noss_wo_freq_feat_og = open("files/uslt_noss_wo_freq_feat_supreme_test.txt","r").read().strip().split('\n') #37.470484
uslt_noss_wo_word_len_feat_og = open("files/uslt_noss_wo_word_len_feat_supreme_test.txt","r").read().strip().split('\n') #37.470484
uslt_zero_og = open("files/uslt_noss_sıfır_deneme_supreme_test.txt","r").read().strip().split('\n') #36.228448
#uslt_noss_og = open("files/uslt_noss_test_supreme.txt","r").read().strip().split('\n') #36.228448
uslt_noss_og = open("files/uslt_noss_yeni_deneme_supreme_test.txt","r").read().strip().split('\n') #36.228448
#uslt_ss_og = open("files/uslt_supreme_test.txt","r").read().strip().split('\n') #37.470484
uslt_ss_og = open("uslt_final_output.txt","r").read().strip().split('\n') #37.470484

scores_array = np.zeros((3,8,5))
for i in range(5):
    low = i*10
    high = (i+1)*10

    input_file = input_file_og[low:high]
    uslt_noss_wo_bert = uslt_noss_wo_bert_og[low:high]
    uslt_noss_wo_lm_loss = uslt_noss_wo_lm_loss_og[low:high]
    uslt_noss_wo_cos_sim = uslt_noss_wo_cos_sim_og[low:high]
    uslt_noss_wo_freq_feat = uslt_noss_wo_freq_feat_og[low:high]
    uslt_noss_wo_word_len_feat = uslt_noss_wo_word_len_feat_og[low:high]
    uslt_zero = uslt_zero_og[low:high]
    uslt_noss = uslt_noss_og[low:high]
    uslt_ss = uslt_ss_og[low:high]
    ref_file1 = ref_file1_og[low:high]
    ref_file2 = ref_file2_og[low:high]
    ref_file3 = ref_file3_og[low:high]

    input_dc = Readability(' '.join(input_file)).dale_chall().score
    uslt_noss_wo_bert_dc = Readability(' '.join(uslt_noss_wo_bert)).dale_chall().score
    uslt_noss_wo_lm_loss_dc = Readability(' '.join(uslt_noss_wo_lm_loss)).dale_chall().score
    uslt_noss_wo_cos_sim_dc = Readability(' '.join(uslt_noss_wo_cos_sim)).dale_chall().score
    uslt_noss_wo_freq_feat_dc = Readability(' '.join(uslt_noss_wo_freq_feat)).dale_chall().score
    uslt_noss_wo_word_len_feat_dc = Readability(' '.join(uslt_noss_wo_word_len_feat)).dale_chall().score
    uslt_zero_dc = Readability(' '.join(uslt_zero)).dale_chall().score
    uslt_noss_dc = Readability(' '.join(uslt_noss)).dale_chall().score
    uslt_dc = Readability(' '.join(uslt_ss)).dale_chall().score

    uslt_noss_wo_bert_fkgl = corpus_fkgl(uslt_noss_wo_bert)
    uslt_noss_wo_lm_loss_fkgl = corpus_fkgl(uslt_noss_wo_lm_loss)
    uslt_noss_wo_cos_sim_fkgl = corpus_fkgl(uslt_noss_wo_cos_sim)
    uslt_noss_wo_freq_feat_fkgl = corpus_fkgl(uslt_noss_wo_freq_feat)
    uslt_noss_wo_word_len_feat_fkgl = corpus_fkgl(uslt_noss_wo_word_len_feat)
    uslt_zero_fkgl = corpus_fkgl(uslt_zero)
    uslt_noss_fkgl = corpus_fkgl(uslt_noss)
    uslt_fkgl = corpus_fkgl(uslt_ss)

# muss_fkgl = Readability(' '.join(muss_test)).flesch_kincaid().score
# access_fkgl = Readability(' '.join(acces_test)).flesch_kincaid().score
# recls_fkgl = Readability(' '.join(recls_outputs)).flesch_kincaid().score
# lsbert_fkgl = Readability(' '.join(lsbert_outputs)).flesch_kincaid().score
# lsbert_ourcwi_fkgl = Readability(' '.join(lsbert_outputs_ourcwi)).flesch_kincaid().score
# tst_fkgl = Readability(' '.join(tst_outputs)).flesch_kincaid().score
# uslt_noss_fkgl = Readability(' '.join(uslt_noss)).flesch_kincaid().score
# uslt_fkgl = Readability(' '.join(uslt_ss)).flesch_kincaid().score

    uslt_noss_wo_bert_sari = corpus_sari(orig_sents=input_file,  
                                        sys_sents=uslt_noss_wo_bert, 
                                        refs_sents=[ref_file1,
                                                    ref_file2,  
                                                    ref_file3])
    uslt_noss_wo_lm_loss_sari = corpus_sari(orig_sents=input_file,  
                                            sys_sents=uslt_noss_wo_lm_loss, 
                                            refs_sents=[ref_file1,
                                                        ref_file2,  
                                                        ref_file3])
    uslt_noss_wo_cos_sim_sari = corpus_sari(orig_sents=input_file,  
                                            sys_sents=uslt_noss_wo_cos_sim, 
                                            refs_sents=[ref_file1,
                                                        ref_file2,  
                                                        ref_file3])
    uslt_noss_wo_freq_feat_sari = corpus_sari(orig_sents=input_file,  
                                            sys_sents=uslt_noss_wo_freq_feat, 
                                            refs_sents=[ref_file1,
                                                        ref_file2,  
                                                        ref_file3])
    uslt_noss_wo_word_len_feat_sari = corpus_sari(orig_sents=input_file,  
                                                sys_sents=uslt_noss_wo_word_len_feat, 
                                                refs_sents=[ref_file1,
                                                            ref_file2,  
                                                            ref_file3])
    uslt_zero_sari = corpus_sari(orig_sents=input_file,
                                 sys_sents=uslt_zero,
                                 refs_sents=[ref_file1,
                                             ref_file2,  
                                             ref_file3])
    uslt_noss_sari = corpus_sari(orig_sents=input_file,  
                                sys_sents=uslt_noss, 
                                refs_sents=[ref_file1,
                                            ref_file2,  
                                            ref_file3])
    uslt_sari = corpus_sari(orig_sents=input_file,  
                            sys_sents=uslt_ss, 
                            refs_sents=[ref_file1,
                                        ref_file2,  
                                        ref_file3])

    score_dict = {"uslt_noss_wo_bert":[uslt_noss_wo_bert_sari,uslt_noss_wo_bert_fkgl,uslt_noss_wo_bert_dc], 
                   "uslt_noss_wo_lm_loss":[uslt_noss_wo_lm_loss_sari,uslt_noss_wo_lm_loss_fkgl,uslt_noss_wo_lm_loss_dc], 
                   "uslt_noss_wo_cos_sim":[uslt_noss_wo_cos_sim_sari,uslt_noss_wo_cos_sim_fkgl,uslt_noss_wo_cos_sim_dc], 
                   "uslt_noss_wo_freq_feat":[uslt_noss_wo_freq_feat_sari,uslt_noss_wo_freq_feat_fkgl,uslt_noss_wo_freq_feat_dc], 
                   "uslt_noss_wo_word_len_feat":[uslt_noss_wo_word_len_feat_sari,uslt_noss_wo_word_len_feat_fkgl,uslt_noss_wo_word_len_feat_dc],
                   "uslt zero":[uslt_zero_sari,uslt_zero_fkgl,uslt_zero_dc], 
                   "uslt no ss":[uslt_noss_sari,uslt_noss_fkgl,uslt_noss_dc], 
                   "uslt":[uslt_sari,uslt_fkgl,uslt_dc]}
    c = 0
    for key in score_dict:
        for metric in range(3):
            scores_array[metric,c,i] = score_dict[key][metric]
        c += 1
    
final_score_dict = np.mean(scores_array,axis=2)
df_means = pd.DataFrame(final_score_dict,index=['SARI', 'FKGL','DC'],columns=['uslt_noss_wo_bert','uslt_noss_wo_lm_loss','uslt_noss_wo_cos_sim','uslt_noss_wo_freq_feat','uslt_noss_wo_word_len_feat','uslt zero', 'uslt no ss','uslt'])
print(df_means)
stds = np.std(scores_array,axis=2)
df_stds = pd.DataFrame(stds,index=['SARI', 'FKGL','DC'],columns=['uslt_noss_wo_bert','uslt_noss_wo_lm_loss','uslt_noss_wo_cos_sim','uslt_noss_wo_freq_feat','uslt_noss_wo_word_len_feat','uslt zero','uslt no ss','uslt'])
print(df_stds)
