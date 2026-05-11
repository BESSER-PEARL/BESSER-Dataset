





import java.util.List;
import java.util.ArrayList;

public class data_Attachment extends Extension {

    private String cachedOnly;
    private String fileIdentifier;
    private String cachedFileUrl;
    private String fileExtension;
    private String fileUrl;
    private String cachedFileName;



    public data_Attachment(
        String cachedOnly,        String fileIdentifier,        String cachedFileUrl,        String fileExtension,        String fileUrl,        String cachedFileName    ) {
        super(
        );
        this.cachedOnly = cachedOnly;
        this.fileIdentifier = fileIdentifier;
        this.cachedFileUrl = cachedFileUrl;
        this.fileExtension = fileExtension;
        this.fileUrl = fileUrl;
        this.cachedFileName = cachedFileName;
    }


    public String getCachedonly() {
        return cachedOnly;
    }

    public void setCachedonly(String cachedOnly) {
        this.cachedOnly = cachedOnly;
    }
    public String getFileidentifier() {
        return fileIdentifier;
    }

    public void setFileidentifier(String fileIdentifier) {
        this.fileIdentifier = fileIdentifier;
    }
    public String getCachedfileurl() {
        return cachedFileUrl;
    }

    public void setCachedfileurl(String cachedFileUrl) {
        this.cachedFileUrl = cachedFileUrl;
    }
    public String getFileextension() {
        return fileExtension;
    }

    public void setFileextension(String fileExtension) {
        this.fileExtension = fileExtension;
    }
    public String getFileurl() {
        return fileUrl;
    }

    public void setFileurl(String fileUrl) {
        this.fileUrl = fileUrl;
    }
    public String getCachedfilename() {
        return cachedFileName;
    }

    public void setCachedfilename(String cachedFileName) {
        this.cachedFileName = cachedFileName;
    }


}