





import java.util.List;
import java.util.ArrayList;

public class types_Import  {

    private String importedNamespace;





    private types_Model types_model;


    public types_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public types_Model getTypes_model() {
        return types_model;
    }

    public void setTypes_model(types_Model types_model) {
        this.types_model = types_model;
    }

}