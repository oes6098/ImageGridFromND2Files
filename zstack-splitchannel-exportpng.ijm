input = getDirectory("Choose a Directory");
list = getFileList(input);
output = input + "Max Projections" + File.separator;

setBatchMode(true);

//Check if output file already exists in this directory
if (File.exists(output)) 
  exit("Destination directory already exists; remove it and then run this macro again");

//Make output file
File.makeDirectory(output);

//Cycle through each image in file
for (i = 0; i < list.length; i++) { 
    if (endsWith(list[i], ".nd2")) {
    	//Open image
        run("Bio-Formats Importer", "open=[" + input + list[i] + "] autoscale color_mode=Colorized rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT");
        
        //Max intensity z projection 
        run("Z Project...", "projection=[Max Intensity]"); 
        imageName = getTitle();
        print(imageName);
        
        //Duplicate image, merge duplicate, then save merged image as png
        run("Duplicate...", "duplicate");
		Property.set("CompositeProjection", "Sum");
		Stack.setDisplayMode("composite");
        saveAs("png", output + (i+1) + getTitle()+"_merge");
        
        //Split original MAX image into separate channels
        selectWindow(imageName);
        run("Split Channels");
        
        //For each channel, adjust brightness, then save as png
        for (j=1; j<4; j++) {
        	splitImageName = "C" + j + "-" + imageName;
        	selectWindow(splitImageName);
        	print(getTitle());
        	
        	//Choose desired min/max values per each channel
        	if (j==1){
        		setMinAndMax(0, 3000);
        		saveAs("png", output + (i+1) + splitImageName);
        	} else {
        		if (j==2){
        			setMinAndMax(0, 32000);
        			saveAs("png", output + (i+1) + splitImageName);
        			//DAPI is 3rd channel, decide whether or not you want it
        		} else {
        			setMinAndMax(0, 300);
        		}
        	}
        	
        }
     
     
     
        }
        close();
    } 
