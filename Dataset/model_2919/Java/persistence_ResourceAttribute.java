





import java.util.List;
import java.util.ArrayList;

public class persistence_ResourceAttribute extends Attribute {

    private int maximumUploadSize;
    private String validUploadExtensions;
    private boolean uploadsWithinWebsite;
    private String validUploadMimeTypes;





    private List<persistence_PathElement> persistence_pathelements;


    public persistence_ResourceAttribute(
        int maximumUploadSize,        String validUploadExtensions,        boolean uploadsWithinWebsite,        String validUploadMimeTypes    ) {
        super(
        );
        this.maximumUploadSize = maximumUploadSize;
        this.validUploadExtensions = validUploadExtensions;
        this.uploadsWithinWebsite = uploadsWithinWebsite;
        this.validUploadMimeTypes = validUploadMimeTypes;
        this.persistence_pathelements = new ArrayList<>();
    }

    public persistence_ResourceAttribute(
        int maximumUploadSize,        String validUploadExtensions,        boolean uploadsWithinWebsite,        String validUploadMimeTypes        ArrayList<persistence_PathElement> persistence_pathelements    ) {
        this.maximumUploadSize = maximumUploadSize;
        this.validUploadExtensions = validUploadExtensions;
        this.uploadsWithinWebsite = uploadsWithinWebsite;
        this.validUploadMimeTypes = validUploadMimeTypes;
        this.persistence_pathelements = persistence_pathelements;
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

    public List<persistence_PathElement> getPersistence_pathelements() {
        return persistence_pathelements;
    }

    public void addPersistence_pathelement(Persistence_pathelement persistence_pathelement) {
        this.persistence_pathelements.add(persistence_pathelement);
    }

}