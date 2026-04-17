#!/usr/bin/env python3

languages = ['Urdu', 'English', 'French', 'German']
languages.append('Spanish')
print(f"Here is the updated list of languages: {languages}")
languages.insert(0, 'Chinese')
print(f"\nHere is the updated list of languages: {languages}")
print(f"\nHere is the Preview of sorted list of languages: {sorted(languages)}")
print(f"\nHere is the Preview of reversed sorted list of languages: {sorted(languages, reverse=True)}")
languages.sort()
print(f"\nHere is the list of languages sorted permanently: {languages}")
print(f"\nHere is the first language in the list: {languages.pop(0)}")
languages.remove('French')
print(f"\nHere is the updated list of languages: {languages}")
del languages[1]
print(f"\nHere is the updated list of languages after deletion: {languages}")
print(f"\nHere is the number of languages in the list: {len(languages)}")