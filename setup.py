from setuptools import setup, find_packages

setup(
    name='encrypted_text_field',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app providing a custom model field for storing sensitive information.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/codingcowde/encrypted_text_field',
    author='codingcow',
    author_email='etf@codingcow.de',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=3.2',
        'cryptography',
    ],
)
