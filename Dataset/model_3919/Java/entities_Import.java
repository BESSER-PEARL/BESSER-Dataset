





import java.util.List;
import java.util.ArrayList;

public class entities_Import  {

    private String importURI;





    private entities_Model entities_model;


    public entities_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public entities_Model getEntities_model() {
        return entities_model;
    }

    public void setEntities_model(entities_Model entities_model) {
        this.entities_model = entities_model;
    }

}