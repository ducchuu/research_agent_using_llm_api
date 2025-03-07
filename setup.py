from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="sci_research_agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=Path("requirements.txt").read_text().splitlines(),
    python_requires=">=3.12",
    description="AI to write shitty scientific research papers",
    author="Mikolaj Duchlinski",
    author_email="mikolaj_duchlinski@gmail.com",
    url="https://github.com/ducchuu/research_agent_using_llm_api",
    license="MIT",
)