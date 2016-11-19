from lib.db.roidb import attach_roidb
from lib.db.maskdb import attach_maskdb
import cPickle

imdb, roidb = attach_roidb('voc_2007_trainval')
#imdb, maskdb = attach_maskdb('voc_2007_trainval')
cache_file = './roidb.pkl'
with open(cache_file, 'wb') as fid:
    cPickle.dump(roidb, fid, cPickle.HIGHEST_PROTOCOL)