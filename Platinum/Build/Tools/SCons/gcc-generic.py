import os

def generate(env, gcc_cross_prefix=None, gcc_strict=True, gcc_stop_on_warning=None, gcc_extra_options=''):
    if gcc_stop_on_warning == None: gcc_stop_on_warning = env['stop_on_warning']

    ### compiler flags
    if gcc_strict:
        env.AppendUnique(CCFLAGS = ['-pedantic', '-Wall',  '-W',  '-Wundef', '-Wno-long-long', '-fPIC'])
        env.AppendUnique(CFLAGS  = ['-Wmissing-prototypes', '-Wmissing-declarations'])
    else:
        env.AppendUnique(CCFLAGS = ['-Wall', '-fPIC'])

    compiler_defines = ['-D_REENTRANT']
    env.AppendUnique(CCFLAGS  = compiler_defines)
    env.AppendUnique(CPPFLAGS = compiler_defines)

    if env['build_config'] == 'Debug':
        env.AppendUnique(CCFLAGS = '-g')
    else:
        env.AppendUnique(CCFLAGS = '-O3')

    if env['target'] != 'universal-apple-macosx':
        env.AppendUnique(CCFLAGS = '-std=c++98')

    if gcc_stop_on_warning:
        env.AppendUnique(CCFLAGS = ['-Werror'])

    env['STRIP']  = 'strip'

    if gcc_cross_prefix:
        env['ENV']['PATH'] += os.environ['PATH']
        env['AR']     = gcc_cross_prefix+'-ar'
        env['RANLIB'] = gcc_cross_prefix+'-ranlib'
        env['CC']     = gcc_cross_prefix+'-gcc ' + gcc_extra_options
        env['CXX']    = gcc_cross_prefix+'-g++ ' + gcc_extra_options
        env['LINK']   = gcc_cross_prefix+'-g++ ' + gcc_extra_options
        env['STRIP']  = gcc_cross_prefix+'-strip'

