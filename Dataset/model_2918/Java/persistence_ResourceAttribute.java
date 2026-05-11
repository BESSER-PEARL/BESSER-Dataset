





import java.util.List;
import java.util.ArrayList;

public class persistence_ResourceAttribute extends EntityAttribute {

    private String validUploadExtensions;
    private int maximumUploadSize;
    private boolean uploadsWithinWebsite;
    private String validUploadMimeTypes;



    public persistence_ResourceAttribute(
        String validUploadExtensions,        int maximumUploadSize,        boolean uploadsWithinWebsite,        String validUploadMimeTypes    ) {
        super(
        );
        this.validUploadExtensions = validUploadExtensions;
        this.maximumUploadSize = maximumUploadSize;
        this.uploadsWithinWebsite = uploadsWithinWebsite;
        this.validUploadMimeTypes = validUploadMimeTypes;
    }


    public String getValiduploadextensions() {
        return validUploadExtensions;
    }

    public void setValiduploadextensions(String validUploadExtensions) {
        this.validUploadExtensions = validUploadExtensions;
    }
    public int getMaximumuploadsize() {
        return maximumUploadSize;
    }

    public void setMaximumuploadsize(int maximumUploadSize) {
        this.maximumUploadSize = maximumUploadSize;
    }
    public boolean getUploadswithinwebsite() {
        return uploadsWithinWebsite;
    }

    public void setUploadswithinwebsite(boolean uploadsWithinWebsite) {
        this.uploadsWithinWebsite = uploadsWithinWebsite;
    }
    public String getValiduploadmimetypes() {
        return validUploadMimeTypes;
    }

    public void setValiduploadmimetypes(String validUploadMimeTypes) {
        this.validUploadMimeTypes = validUploadMimeTypes;
    }


}