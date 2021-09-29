#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Configuration
import os
import re
from copy import deepcopy


class ProvPath:
    root = os.path.dirname(os.path.abspath(__file__))

    fdir_data = os.path.sep.join((root, 'data'))
    fdir_corpus = os.path.sep.join((root, 'corpus'))
    fdir_model = os.path.sep.join((root, 'model'))


class ProvFunc:
    def normalize(self, text, do_lower=True, do_marking=True):
        if do_lower:
            text = deepcopy(text.lower())
        else:
            pass

        if do_marking:
            sent = text.split()
            for i, w in enumerate(sent):
                if re.match('www.', str(w)):
                    sent[i] = 'URL'
                elif re.search('\d+\d\.\d+', str(w)):
                    sent[i] = 'REF'
                elif re.match('\d', str(w)):
                    sent[i] = 'NUM'
                else:
                    continue

            text = deepcopy(' '.join(sent))
            del sent
        else:
            pass

        text = text.replace('?', '')
        text = re.sub('[^ \'\?\./0-9a-zA-Zㄱ-힣\n]', '', text)

        text = text.replace(' / ', '/')
        text = re.sub('\.+\.', ' ', text)
        text = text.replace('\\\\', '\\').replace('\\r\\n', '')
        text = text.replace('\n', '  ')
        text = re.sub('\. ', '  ', text)
        text = re.sub('\s+\s', ' ', text).strip()

        return text