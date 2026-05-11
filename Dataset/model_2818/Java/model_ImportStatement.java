





import java.util.List;
import java.util.ArrayList;

public class model_ImportStatement  {

    private String importedNamespace;



    public model_ImportStatement(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }


}