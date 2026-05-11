





import java.util.List;
import java.util.ArrayList;

public class gaml_Import extends VarDefinition {

    private String importURI;





    private gaml_Model gaml_model;


    public gaml_Import(
        String importURI    ) {
        super(
        );
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public gaml_Model getGaml_model() {
        return gaml_model;
    }

    public void setGaml_model(gaml_Model gaml_model) {
        this.gaml_model = gaml_model;
    }

}