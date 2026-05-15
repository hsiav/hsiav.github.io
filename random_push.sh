#!/usr/bin/env bash
set -e

echo "===== AUTO UPDATE START ====="

# 站點列表（你可以按需求加入或移除）
sites=(
  "CN|/c/Users/eric/Desktop/aff_folder/hsiav.github.io|master|index.md Readme.md image/speed_test/vpn_speed_test_combined.png"
  "ES|/c/Users/eric/Desktop/aff_folder/vpn-mundo.github.io|master|."
  "EN|/c/Users/eric/Desktop/aff_folder/VPNuniverse.github.io|master|."
  "JP|/c/Users/eric/Desktop/aff_folder/vpn-hikaku-lab.github.io|master|."
  "DE|/c/Users/eric/Desktop/aff_folder/clean/vpn-welt.github.io|main|."
)

# 隨機選 2 個站
selected=($(shuf -e "${sites[@]}" -n 2))

for item in "${selected[@]}"; do
  IFS="|" read -r name path branch addfiles <<< "$item"

  echo ">>> Update ${name} site"
  cd "$path"

  # CN 站才需要跑 run_scripts.sh
  if [[ "$name" == "CN" ]]; then
    ./run_scripts.sh
  fi

  # 暫停一下，避免太像機器
  sleep $((RANDOM % 60 + 30))

  git add $addfiles

  if git diff --cached --quiet; then
    echo "${name} site: no changes, skip commit"
  else
    git commit -m "${name} auto update ($(date +'%Y-%m-%d'))"
    git push origin "$branch"
  fi

  echo "===== ${name} AUTO UPDATE DONE ====="
done

echo "===== AUTO UPDATE COMPLETE ====="
