import setuptools

setuptools.setup(
    name='chatgpt-integration',
    version='1.0.0',
    author='Paola Cartala',
    description='A Django web application for integrating\
    ChatGPT for question and answer.',
    packages=setuptools.find_packages(exclude='tests'),
    scripts=['manage.py'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
