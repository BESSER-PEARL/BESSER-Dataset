





import java.util.List;
import java.util.ArrayList;

public class model_attachment_FileAttachment extends Attachment {

    private String fileHash;
    private String fileID;
    private String fileName;
    private String fileSize;
    private boolean requiredOffline;



    public model_attachment_FileAttachment(
        String fileHash,        String fileID,        String fileName,        String fileSize,        boolean requiredOffline    ) {
        super(
        );
        this.fileHash = fileHash;
        this.fileID = fileID;
        this.fileName = fileName;
        this.fileSize = fileSize;
        this.requiredOffline = requiredOffline;
    }


    public String getFilehash() {
        return fileHash;
    }

    public void setFilehash(String fileHash) {
        this.fileHash = fileHash;
    }
    public String getFileid() {
        return fileID;
    }

    public void setFileid(String fileID) {
        this.fileID = fileID;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getFilesize() {
        return fileSize;
    }

    public void setFilesize(String fileSize) {
        this.fileSize = fileSize;
    }
    public boolean getRequiredoffline() {
        return requiredOffline;
    }

    public void setRequiredoffline(boolean requiredOffline) {
        this.requiredOffline = requiredOffline;
    }


}