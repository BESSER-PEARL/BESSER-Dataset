





import java.util.List;
import java.util.ArrayList;

public class data_Attachment extends Extension {

    private String cachedFileName;
    private String cachedOnly;
    private String fileUrl;
    private String cachedFileUrl;
    private String fileIdentifier;
    private String fileExtension;



    public data_Attachment(
        String cachedFileName,        String cachedOnly,        String fileUrl,        String cachedFileUrl,        String fileIdentifier,        String fileExtension    ) {
        super(
        );
        this.cachedFileName = cachedFileName;
        this.cachedOnly = cachedOnly;
        this.fileUrl = fileUrl;
        this.cachedFileUrl = cachedFileUrl;
        this.fileIdentifier = fileIdentifier;
        this.fileExtension = fileExtension;
    }


    public String getCachedfilename() {
        return cachedFileName;
    }

    public void setCachedfilename(String cachedFileName) {
        this.cachedFileName = cachedFileName;
    }
    public String getCachedonly() {
        return cachedOnly;
    }

    public void setCachedonly(String cachedOnly) {
        this.cachedOnly = cachedOnly;
    }
    public String getFileurl() {
        return fileUrl;
    }

    public void setFileurl(String fileUrl) {
        this.fileUrl = fileUrl;
    }
    public String getCachedfileurl() {
        return cachedFileUrl;
    }

    public void setCachedfileurl(String cachedFileUrl) {
        this.cachedFileUrl = cachedFileUrl;
    }
    public String getFileidentifier() {
        return fileIdentifier;
    }

    public void setFileidentifier(String fileIdentifier) {
        this.fileIdentifier = fileIdentifier;
    }
    public String getFileextension() {
        return fileExtension;
    }

    public void setFileextension(String fileExtension) {
        this.fileExtension = fileExtension;
    }


}