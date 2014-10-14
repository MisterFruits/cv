from os import listdir
import re

topdir = '.'
outdir = '%s/target' % topdir
srcdir = '%s/src' % topdir

TEX_FILE_MATCHER = re.compile(r'.*\.tex$')


def configure(conf):
    conf.load('tex')
    if not conf.env.LATEX:
        conf.fatal('The program LaTex is required')

def build(bld):
    for filename in listfiles(srcdir, TEX_FILE_MATCHER):
        pdflatex(bld, '%s/%s' % (srcdir, filename))
    # print(listfiles(srcdir, TEX_FILE_MATCHER))
    # pdflatex(bld, '%s/%s' % (srcdir, "cv_victor.tex"))

def pdflatex(bld, src):
    bld(
        features = 'tex',
        type     = 'pdflatex', # pdflatex or xelatex
        source   = src,  # mandatory, the source
        outs     = 'pdf', # 'pdf' or 'ps pdf'
        # deps     = 'crossreferencing.lst', # to give dependencies directly
        prompt   = 0, # 0 for the batch mode, 1 otherwise
        )

def listfiles(dir, matcher=re.compile(r'.*')):
    return [filename for filename in listdir(dir) if matcher.match(filename)]
