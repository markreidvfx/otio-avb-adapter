# Copyright Contributors to the OpenTimelineIO project
#
# SPDX-License-Identifier: MIT OR Apache-2.0
#

import io
import setuptools

with io.open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="otio-avb-adapter",
    author="Mark Reid",
    author_email="mindmark@gmail.com",
    version="0.0.1",
    description="OpenTimelineIO Avid Bin (AVB) Adapter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Replace url with your repo
    url="https://github.com/markreidvfx/otio-avb-adapter",
    platforms='any',
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        "opentimelineio.plugins": "otio_avb_adapter = otio_avb_adapter"
    },
    package_data={
        "otio_avb_adapter": [
            "plugin_manifest.json",
        ],
    },
    install_requires=[
        "OpenTimelineIO>=0.14.1",
        "pyavb>=1.2.0",
    ],
    extras_require={
        "dev": [
            "flake8",
            "pytest",
            "pytest-cov",
            "twine"
        ]
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*,' + \
                    '!=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Display",
        "Topic :: Multimedia :: Video :: Non-Linear Editor",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English"
    ]
)
