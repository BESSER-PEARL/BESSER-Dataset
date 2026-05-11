





import java.util.List;
import java.util.ArrayList;

public class data_Attachment extends Extension {

    private String cachedFileName;
    private String cachedFileUrl;
    private String fileIdentifier;
    private String fileUrl;
    private String cachedOnly;
    private String fileExtension;
    private String noCache;



    public data_Attachment(
        String cachedFileName,        String cachedFileUrl,        String fileIdentifier,        String fileUrl,        String cachedOnly,        String fileExtension,        String noCache    ) {
        super(
        );
        this.cachedFileName = cachedFileName;
        this.cachedFileUrl = cachedFileUrl;
        this.fileIdentifier = fileIdentifier;
        this.fileUrl = fileUrl;
        this.cachedOnly = cachedOnly;
        this.fileExtension = fileExtension;
        this.noCache = noCache;
    }


    public String getCachedfilename() {
        return cachedFileName;
    }

    public void setCachedfilename(String cachedFileName) {
        this.cachedFileName = cachedFileName;
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
    public String getFileurl() {
        return fileUrl;
    }

    public void setFileurl(String fileUrl) {
        this.fileUrl = fileUrl;
    }
    public String getCachedonly() {
        return cachedOnly;
    }

    public void setCachedonly(String cachedOnly) {
        this.cachedOnly = cachedOnly;
    }
    public String getFileextension() {
        return fileExtension;
    }

    public void setFileextension(String fileExtension) {
        this.fileExtension = fileExtension;
    }
    public String getNocache() {
        return noCache;
    }

    public void setNocache(String noCache) {
        this.noCache = noCache;
    }


}