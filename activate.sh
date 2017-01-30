# run with `source activate.sh`
if [ ! -d ~/SemanticWebEnv ]; then
	virtualenv --python=python3 ~/SemanticWebEnv
fi
source ~/SemanticWebEnv/bin/activate
pip3 install -r requirements.txt
