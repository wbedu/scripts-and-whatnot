#!/usr/bin/env bash


printer="airscan:e0:Brother HL-L2395DW series"
dest_dir=$HOME"/scans/"
mkdir -p $dest_dir
output_file=$dest_dir`date +"%d-%m-%Y-%H-%M-%S"`".tiff"
echo scanning to $output_file
{
scanimage -d $printer \
 					--output-file=$output_file \
					--format=tiff
} ||{
	
#return if fail
scanimage -d $printer \
	 					--output-file=$output_file \
						--format=tiff

}
