





import java.util.List;
import java.util.ArrayList;

public class model_attachment_FileAttachment extends Attachment {

    private boolean downloading;
    private String fileType;
    private boolean uploading;
    private String fileSize;
    private String fileID;
    private String fileHash;
    private boolean requiredOffline;
    private String fileName;



    public model_attachment_FileAttachment(
        boolean downloading,        String fileType,        boolean uploading,        String fileSize,        String fileID,        String fileHash,        boolean requiredOffline,        String fileName    ) {
        super(
        );
        this.downloading = downloading;
        this.fileType = fileType;
        this.uploading = uploading;
        this.fileSize = fileSize;
        this.fileID = fileID;
        this.fileHash = fileHash;
        this.requiredOffline = requiredOffline;
        this.fileName = fileName;
    }


    public boolean getDownloading() {
        return downloading;
    }

    public void setDownloading(boolean downloading) {
        this.downloading = downloading;
    }
    public String getFiletype() {
        return fileType;
    }

    public void setFiletype(String fileType) {
        this.fileType = fileType;
    }
    public boolean getUploading() {
        return uploading;
    }

    public void setUploading(boolean uploading) {
        this.uploading = uploading;
    }
    public String getFilesize() {
        return fileSize;
    }

    public void setFilesize(String fileSize) {
        this.fileSize = fileSize;
    }
    public String getFileid() {
        return fileID;
    }

    public void setFileid(String fileID) {
        this.fileID = fileID;
    }
    public String getFilehash() {
        return fileHash;
    }

    public void setFilehash(String fileHash) {
        this.fileHash = fileHash;
    }
    public boolean getRequiredoffline() {
        return requiredOffline;
    }

    public void setRequiredoffline(boolean requiredOffline) {
        this.requiredOffline = requiredOffline;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }


}