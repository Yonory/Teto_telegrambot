#!/bin/bash

BASE_URL="https://archive.org/download/f4576ad6932d7da27e8441478e0e3ae0"
IMAGES_DIR="images"

cd $IMAGES_DIR

echo "Скачиваю арты Тето..."

# Продолжаем нумерацию с 21
wget -q --show-progress "$BASE_URL/cheonha87.jpg" -O teto_21.jpg
wget -q --show-progress "$BASE_URL/dpzkzl.jpg" -O teto_22.jpg
wget -q --show-progress "$BASE_URL/e20.jpg" -O teto_23.jpg
wget -q --show-progress "$BASE_URL/fejnkm.jpg" -O teto_24.jpg
wget -q --show-progress "$BASE_URL/ferus.jpg" -O teto_25.jpg
wget -q --show-progress "$BASE_URL/hanbu.jpg" -O teto_26.jpg
wget -q --show-progress "$BASE_URL/kaede.jpg" -O teto_27.jpg
wget -q --show-progress "$BASE_URL/kaninn.jpg" -O teto_28.jpg
wget -q --show-progress "$BASE_URL/katzeh.jpg" -O teto_29.jpg
wget -q --show-progress "$BASE_URL/keimari.jpg" -O teto_30.jpg
wget -q --show-progress "$BASE_URL/kiyuren.jpg" -O teto_31.jpg
wget -q --show-progress "$BASE_URL/kondoru.jpg" -O teto_32.jpg
wget -q --show-progress "$BASE_URL/konpasu.jpg" -O teto_33.jpg
wget -q --show-progress "$BASE_URL/lilium.jpg" -O teto_34.jpg
wget -q --show-progress "$BASE_URL/mikeco%202.jpg" -O teto_35.jpg
wget -q --show-progress "$BASE_URL/mikeco%203.jpg" -O teto_36.jpg
wget -q --show-progress "$BASE_URL/minami%202.jpg" -O teto_37.jpg
wget -q --show-progress "$BASE_URL/minami%203.jpg" -O teto_38.jpg
wget -q --show-progress "$BASE_URL/miyako.jpg" -O teto_39.jpg
wget -q --show-progress "$BASE_URL/mji.jpg" -O teto_40.jpg
wget -q --show-progress "$BASE_URL/mukki.jpg" -O teto_41.jpg
wget -q --show-progress "$BASE_URL/n-tai.jpg" -O teto_42.jpg
wget -q --show-progress "$BASE_URL/neg.jpg" -O teto_43.jpg
wget -q --show-progress "$BASE_URL/oumi%20sanaka.jpg" -O teto_44.jpg
wget -q --show-progress "$BASE_URL/pikopeko.jpg" -O teto_45.jpg
wget -q --show-progress "$BASE_URL/riot.jpg" -O teto_46.jpg
wget -q --show-progress "$BASE_URL/shell518.jpg" -O teto_47.jpg
wget -q --show-progress "$BASE_URL/shou%20shishi.jpg" -O teto_48.jpg
wget -q --show-progress "$BASE_URL/takunama.jpg" -O teto_49.jpg
wget -q --show-progress "$BASE_URL/uli.jpg" -O teto_50.jpg

echo ""
echo "Готово! Скачано ещё 30 изображений"
echo "Всего в галерее:"
ls -1 | wc -l
