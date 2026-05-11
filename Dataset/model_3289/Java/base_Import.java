





import java.util.List;
import java.util.ArrayList;

public class base_Import  {

    private String importURI;
    private String importedNamespace;



    public base_Import(
        String importURI,        String importedNamespace    ) {
        this.importURI = importURI;
        this.importedNamespace = importedNamespace;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }
    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }


}