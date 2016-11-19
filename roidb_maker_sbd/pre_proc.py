from lib.db.roidb import attach_roidb
from lib.db.maskdb import attach_maskdb
import cPickle

imdb, roidb = attach_roidb('voc_2012_seg_train')
imdb, maskdb = attach_maskdb('voc_2012_seg_train')
cache_file = './roidb.pkl'
mask_cache_file = './maskdb.pkl'
with open(cache_file, 'wb') as fid:
    cPickle.dump(roidb, fid, cPickle.HIGHEST_PROTOCOL)

with open(mask_cache_file, 'wb') as fidmask:
    cPickle.dump(maskdb, fidmask, cPickle.HIGHEST_PROTOCOL)