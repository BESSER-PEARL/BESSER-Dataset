





import java.util.List;
import java.util.ArrayList;

public class builderState_ResourceDescription  {

    private String importedNames;
    private String URI;



    public builderState_ResourceDescription(
        String importedNames,        String URI    ) {
        this.importedNames = importedNames;
        this.URI = URI;
    }


    public String getImportednames() {
        return importedNames;
    }

    public void setImportednames(String importedNames) {
        this.importedNames = importedNames;
    }
    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }


}