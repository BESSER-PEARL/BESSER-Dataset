





import java.util.List;
import java.util.ArrayList;

public class model_attachment_FileAttachment extends Attachment {

    private String fileName;
    private boolean requiredOffline;
    private String fileSize;
    private String fileID;
    private String fileHash;



    public model_attachment_FileAttachment(
        String fileName,        boolean requiredOffline,        String fileSize,        String fileID,        String fileHash    ) {
        super(
        );
        this.fileName = fileName;
        this.requiredOffline = requiredOffline;
        this.fileSize = fileSize;
        this.fileID = fileID;
        this.fileHash = fileHash;
    }


    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public boolean getRequiredoffline() {
        return requiredOffline;
    }

    public void setRequiredoffline(boolean requiredOffline) {
        this.requiredOffline = requiredOffline;
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


}