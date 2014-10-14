topdir = '.'
outdir = '%s/target' % topdir
srcdir = '%s/src' % topdir


def configure(conf):
    conf.load('tex')
    if not conf.env.LATEX:
        conf.fatal('The program LaTex is required')

def build(bld):
    bld(
        features = 'tex',
        type     = 'pdflatex', # pdflatex or xelatex
        source   = '%s/cv_victor.tex' % srcdir,  # mandatory, the source
        outs     = 'pdf', # 'pdf' or 'ps pdf'
        # deps     = 'crossreferencing.lst', # to give dependencies directly
        prompt   = 1, # 0 for the batch mode
        )
