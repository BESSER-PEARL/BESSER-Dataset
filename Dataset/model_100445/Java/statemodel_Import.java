





import java.util.List;
import java.util.ArrayList;

public class statemodel_Import  {

    private String importURI;





    private statemodel_Model statemodel_model;


    public statemodel_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public statemodel_Model getStatemodel_model() {
        return statemodel_model;
    }

    public void setStatemodel_model(statemodel_Model statemodel_model) {
        this.statemodel_model = statemodel_model;
    }

}