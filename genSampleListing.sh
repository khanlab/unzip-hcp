#!/bin/bash

in_hcp_dir=/project/6050199/ext-data/hcp1200/zipfiles
mkdir -p sample_file_listing

testsubj=100610
for zip in `ls $in_hcp_dir/${testsubj}*.zip`
do
    zip_name=${zip##*${testsubj}_}
    zip_name=${zip_name%.zip}
    unzip -l $zip | sed "s/$testsubj/{subject}/g" | tee sample_file_listing/${zip_name}.txt
    echo ""
    echo ""
done 
