# #!/usr/bin/env bash
# set -e

# # 先切到 repo
# cd "$(dirname "$0")"

# # 如果你本來有更新的 bash，在這裡跑
# ./run_scripts.sh

# # 固定加入三個檔案
# git add index.md
# git add Readme.md
# git add image/speed_test/vpn_speed_test_combined.png

# # commit + push
# git commit -m "auto update"
# git push


########### update version for both sites

#!/usr/bin/env bash
set -e

echo "===== AUTO UPDATE START ====="

################################
# 中文站
################################
echo ">>> Update CN site"
cd /c/Users/eric/Desktop/aff_folder/hsiav.github.io

./run_scripts.sh

git add index.md Readme.md image/speed_test/vpn_speed_test_combined.png

if git diff --cached --quiet; then
  echo "CN site: no changes, skip commit"
else
  git commit -m "CN auto update ($(date +'%Y-%m-%d'))"
  git push origin master
fi

################################
# 英文站
################################
echo ">>> Update ES site"
cd /c/Users/eric/Desktop/aff_folder/vpn-mundo.github.io

# python daily_speedtest.py

git add .

if git diff --cached --quiet; then
  echo "EN site: no changes, skip commit"
else
  git commit -m "EN auto update ($(date +'%Y-%m-%d'))"
  git push origin master
fi

echo "===== AUTO UPDATE DONE ====="
