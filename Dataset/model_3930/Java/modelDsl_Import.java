





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Import  {

    private String importedNamespace;





    private modelDsl_Model modeldsl_model;


    public modelDsl_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public modelDsl_Model getModeldsl_model() {
        return modeldsl_model;
    }

    public void setModeldsl_model(modelDsl_Model modeldsl_model) {
        this.modeldsl_model = modeldsl_model;
    }

}