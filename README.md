Endnote journal abbreviations term list 
=======================================
Since journal abbreviations are requested under certain circumstances but Endnote builtin journal term list did not cover many common journals, especially for new journals and those related to Engineering, it is necessary to import customized journal term list. 

### HOWTO
1. Prepare term list(s), separate journal name and abbr. by <kbd>tab</kbd>.  
   Here a list derived from [UBC library](https://woodward.library.ubc.ca/research-help/journal-abbreviations/) containing common engineering journal abbreviations is provided. Chemical/BioScience/Physics journal abbreviations lists from Endnote presets are also provided.
2. Modify and run `export_terms.py`, the script will output a merged term list. Or just download provided `merged.txt`.
3. In Endnote, import merged term list by `Tools` -> `Open Term Lists` -> `Journals Term List` -> `Lists` -> `Import List...`. Now Endnote should support conversion between full journal name and abbr.
4. To specify whether use abbr. in citation, chose one style by `Edit` -> `Output Styles` -> `Edit `_style in use_ -> `Journal Names`.

#### Reference
[理工科的Journal Term Lists](http://blog.sciencenet.cn/blog-2148673-1096454.html)