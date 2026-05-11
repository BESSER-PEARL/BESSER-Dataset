





import java.util.List;
import java.util.ArrayList;

public class ric_Portal  {

    private String documentsExtension;
    private String name;



    public ric_Portal(
        String documentsExtension,        String name    ) {
        this.documentsExtension = documentsExtension;
        this.name = name;
    }


    public String getDocumentsextension() {
        return documentsExtension;
    }

    public void setDocumentsextension(String documentsExtension) {
        this.documentsExtension = documentsExtension;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}