'''Version info'''

short_version = '2.3'
'''Short version in the form of N.N'''

__version__ = short_version + 'a1'
'''Version in the form of N.N[.N]+[{a|b|c|rc}N[.N]+][.postN][.devN]'''


__all__ = ['short_version', '__version__']


if __name__ == '__main__':
    print(__version__, end='')
