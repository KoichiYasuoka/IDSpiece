import os,setuptools
with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/IDSpiece"

setuptools.setup(
  name="idspiece",
  version="0.6.4",
  description="Ideographic Tokenizer with CHISE-IDS",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="GPL",
  keywords="NLP Chinese",
  packages=setuptools.find_packages(),
  python_requires=">=3.6",
  classifiers=[
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic"
  ],
  project_urls={
    "CHISE":"https://www.chise.org/ids/",
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
