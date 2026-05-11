





import java.util.List;
import java.util.ArrayList;

public class ric_Portal  {

    private String name;
    private String documentsExtension;



    public ric_Portal(
        String name,        String documentsExtension    ) {
        this.name = name;
        this.documentsExtension = documentsExtension;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentsextension() {
        return documentsExtension;
    }

    public void setDocumentsextension(String documentsExtension) {
        this.documentsExtension = documentsExtension;
    }


}