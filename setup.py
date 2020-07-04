from distutils.core import setup
setup(
  name = 'macos-releases',
  version = '1.0',
  license='MIT',
  description = 'Get the name and version of a macOS releases',
  author = 'XIMet',
  author_email = 'dq.ximet@gmail.com',
  url = 'https://github.com/ximet/macos-releases',
  download_url = 'https://github.com/ximet/macos-releases/archive/v1.0.tar.gz',
  keywords = ['MACOS', 'VERSION', 'DARWIN'],
  install_requires=['os'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)