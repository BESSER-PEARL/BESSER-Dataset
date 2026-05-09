





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Import  {

    private String importedNamespace;



    public appBuilderDSL_Import(
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