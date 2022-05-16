#!/usr/bin/env python
# coding: utf-8

import json


if __name__ == "__main__":
    with open("data/output.json") as f:
        data = json.load(f)
        new_data = data['rows'][0]['doc']['historical_analysis']
        
        
    with open('data/processed.json', 'w') as fp:
        json.dump(new_data, fp)
                



