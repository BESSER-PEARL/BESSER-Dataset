





import java.util.List;
import java.util.ArrayList;

public class model_attachment_FileAttachment extends Attachment {

    private boolean requiredOffline;
    private String fileName;
    private String fileHash;
    private String fileID;
    private String fileSize;



    public model_attachment_FileAttachment(
        boolean requiredOffline,        String fileName,        String fileHash,        String fileID,        String fileSize    ) {
        super(
        );
        this.requiredOffline = requiredOffline;
        this.fileName = fileName;
        this.fileHash = fileHash;
        this.fileID = fileID;
        this.fileSize = fileSize;
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
    public String getFilesize() {
        return fileSize;
    }

    public void setFilesize(String fileSize) {
        this.fileSize = fileSize;
    }


}