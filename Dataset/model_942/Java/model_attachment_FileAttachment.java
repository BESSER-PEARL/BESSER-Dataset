





import java.util.List;
import java.util.ArrayList;

public class model_attachment_FileAttachment extends Attachment {

    private String fileID;
    private boolean requiredOffline;
    private String fileName;
    private String fileSize;
    private String fileHash;



    public model_attachment_FileAttachment(
        String fileID,        boolean requiredOffline,        String fileName,        String fileSize,        String fileHash    ) {
        super(
        );
        this.fileID = fileID;
        this.requiredOffline = requiredOffline;
        this.fileName = fileName;
        this.fileSize = fileSize;
        this.fileHash = fileHash;
    }


    public String getFileid() {
        return fileID;
    }

    public void setFileid(String fileID) {
        this.fileID = fileID;
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
    public String getFilesize() {
        return fileSize;
    }

    public void setFilesize(String fileSize) {
        this.fileSize = fileSize;
    }
    public String getFilehash() {
        return fileHash;
    }

    public void setFilehash(String fileHash) {
        this.fileHash = fileHash;
    }


}