





import java.util.List;
import java.util.ArrayList;

public class DocumentStorage  {

    private int id;
    private String documentPath;
    private boolean is_exist;
    private int documentCode;



    public DocumentStorage(
        int id,        String documentPath,        boolean is_exist,        int documentCode    ) {
        this.id = id;
        this.documentPath = documentPath;
        this.is_exist = is_exist;
        this.documentCode = documentCode;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDocumentpath() {
        return documentPath;
    }

    public void setDocumentpath(String documentPath) {
        this.documentPath = documentPath;
    }
    public boolean getIs_exist() {
        return is_exist;
    }

    public void setIs_exist(boolean is_exist) {
        this.is_exist = is_exist;
    }
    public int getDocumentcode() {
        return documentCode;
    }

    public void setDocumentcode(int documentCode) {
        this.documentCode = documentCode;
    }


}