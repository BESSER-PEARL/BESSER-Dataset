





import java.util.List;
import java.util.ArrayList;

public class model_attachment_FileAttachment extends Attachment {

    private String fileHash;
    private boolean requiredOffline;
    private String fileName;
    private String fileID;
    private String fileSize;
    private boolean downloading;
    private boolean uploading;
    private String fileType;



    public model_attachment_FileAttachment(
        String fileHash,        boolean requiredOffline,        String fileName,        String fileID,        String fileSize,        boolean downloading,        boolean uploading,        String fileType    ) {
        super(
        );
        this.fileHash = fileHash;
        this.requiredOffline = requiredOffline;
        this.fileName = fileName;
        this.fileID = fileID;
        this.fileSize = fileSize;
        this.downloading = downloading;
        this.uploading = uploading;
        this.fileType = fileType;
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
    public String getFileid() {
        return fileID;
    }

    public void setFileid(String fileID) {
        this.fileID = fileID;
    }
    public String getFilesize() {
        return fileSize;
    }

    public void setFilesize(String fileSize) {
        this.fileSize = fileSize;
    }
    public boolean getDownloading() {
        return downloading;
    }

    public void setDownloading(boolean downloading) {
        this.downloading = downloading;
    }
    public boolean getUploading() {
        return uploading;
    }

    public void setUploading(boolean uploading) {
        this.uploading = uploading;
    }
    public String getFiletype() {
        return fileType;
    }

    public void setFiletype(String fileType) {
        this.fileType = fileType;
    }


}