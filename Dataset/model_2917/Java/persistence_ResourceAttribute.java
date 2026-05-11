





import java.util.List;
import java.util.ArrayList;

public class persistence_ResourceAttribute extends EntityAttribute {

    private boolean uploadsWithinWebsite;
    private int maximumUploadSize;
    private String validUploadExtensions;
    private String validUploadMimeTypes;



    public persistence_ResourceAttribute(
        boolean uploadsWithinWebsite,        int maximumUploadSize,        String validUploadExtensions,        String validUploadMimeTypes    ) {
        super(
        );
        this.uploadsWithinWebsite = uploadsWithinWebsite;
        this.maximumUploadSize = maximumUploadSize;
        this.validUploadExtensions = validUploadExtensions;
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


}