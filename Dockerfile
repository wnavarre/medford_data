FROM ubuntu:24.04
RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y\
        git \
        curl \
        && \
    apt autoremove -y
RUN cd ~ && \
    mkdir -p ~/.miniconda3 && \
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/.miniconda3/miniconda.sh && \
    bash ~/.miniconda3/miniconda.sh -b -u -p ~/.miniconda3 && \
    rm -rf ~/.miniconda3/miniconda.sh
RUN true && \
	export PATH=/root/.miniconda3/bin:$PATH && \
    yes | conda create -n GEO_ENV python=3.10 && \
    echo "source activate GEO_ENV" >> ~/.bashrc
ENV PATH /root/.miniconda3/bin:$PATH
RUN activate GEO_ENV && \
	conda install --name GEO_ENV --yes ipython && \
	conda install --name GEO_ENV --yes --channel conda-forge geopandas && \
	conda install --name GEO_ENV --yes --channel conda-forge fiona && \
    conda install --name GEO_ENV --yes --channel conda-forge poppler
RUN apt-get install make
RUN conda install --name GEO_ENV --yes --channel conda-forge pyarrow
RUN apt-get install unzip