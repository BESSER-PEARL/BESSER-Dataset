





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_Attachment  {

    private String contentType;
    private String fileName;
    private String name;
    private String fileData;
    private String id;
    private String size;



    public org_aries_common_Attachment(
        String contentType,        String fileName,        String name,        String fileData,        String id,        String size    ) {
        this.contentType = contentType;
        this.fileName = fileName;
        this.name = name;
        this.fileData = fileData;
        this.id = id;
        this.size = size;
    }


    public String getContenttype() {
        return contentType;
    }

    public void setContenttype(String contentType) {
        this.contentType = contentType;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFiledata() {
        return fileData;
    }

    public void setFiledata(String fileData) {
        this.fileData = fileData;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}