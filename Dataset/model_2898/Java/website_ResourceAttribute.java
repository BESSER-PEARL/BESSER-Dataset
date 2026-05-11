





import java.util.List;
import java.util.ArrayList;

public class website_ResourceAttribute extends EntityAttribute {

    private String validUploadExtensions;
    private String validUploadMimeTypes;
    private boolean uploadsWithinWebsite;
    private int maximumUploadSize;



    public website_ResourceAttribute(
        String validUploadExtensions,        String validUploadMimeTypes,        boolean uploadsWithinWebsite,        int maximumUploadSize    ) {
        super(
        );
        this.validUploadExtensions = validUploadExtensions;
        this.validUploadMimeTypes = validUploadMimeTypes;
        this.uploadsWithinWebsite = uploadsWithinWebsite;
        this.maximumUploadSize = maximumUploadSize;
    }


    public String getValiduploadextensions() {
        return validUploadExtensions;
    }

    public void setValiduploadextensions(String validUploadExtensions) {
        this.validUploadExtensions = validUploadExtensions;
    }
    public String getValiduploadmimetypes() {
        return validUploadMimeTypes;
    }

    public void setValiduploadmimetypes(String validUploadMimeTypes) {
        this.validUploadMimeTypes = validUploadMimeTypes;
    }
    public boolean getUploadswithinwebsite() {
        return uploadsWithinWebsite;
    }

    public void setUploadswithinwebsite(boolean uploadsWithinWebsite) {
        this.uploadsWithinWebsite = uploadsWithinWebsite;
    }
    public int getMaximumuploadsize() {
        return maximumUploadSize;
    }

    public void setMaximumuploadsize(int maximumUploadSize) {
        this.maximumUploadSize = maximumUploadSize;
    }


}