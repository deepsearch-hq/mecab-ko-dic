#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
mecab -d $DIR/../ -F "%m\t%f[0],%phl,%phr,%pb,%pw,%pC,%pc,%pn\n" -N5
