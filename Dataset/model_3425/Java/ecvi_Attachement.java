





import java.util.List;
import java.util.ArrayList;

public class ecvi_Attachement  {

    private String filename;
    private String comment;
    private String payload;
    private String mimeType;
    private String docType;



    public ecvi_Attachement(
        String filename,        String comment,        String payload,        String mimeType,        String docType    ) {
        this.filename = filename;
        this.comment = comment;
        this.payload = payload;
        this.mimeType = mimeType;
        this.docType = docType;
    }


    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getPayload() {
        return payload;
    }

    public void setPayload(String payload) {
        this.payload = payload;
    }
    public String getMimetype() {
        return mimeType;
    }

    public void setMimetype(String mimeType) {
        this.mimeType = mimeType;
    }
    public String getDoctype() {
        return docType;
    }

    public void setDoctype(String docType) {
        this.docType = docType;
    }


}