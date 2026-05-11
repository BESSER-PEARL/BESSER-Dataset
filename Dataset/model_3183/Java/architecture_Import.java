





import java.util.List;
import java.util.ArrayList;

public class architecture_Import  {

    private String importedNamespace;





    private architecture_AbstractModel architecture_abstractmodel;


    public architecture_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public architecture_AbstractModel getArchitecture_abstractmodel() {
        return architecture_abstractmodel;
    }

    public void setArchitecture_abstractmodel(architecture_AbstractModel architecture_abstractmodel) {
        this.architecture_abstractmodel = architecture_abstractmodel;
    }

}