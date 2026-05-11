





import java.util.List;
import java.util.ArrayList;

public class sadl_Import  {

    private String alias;
    private String importURI;





    private sadl_Model sadl_model;


    public sadl_Import(
        String alias,        String importURI    ) {
        this.alias = alias;
        this.importURI = importURI;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public sadl_Model getSadl_model() {
        return sadl_model;
    }

    public void setSadl_model(sadl_Model sadl_model) {
        this.sadl_model = sadl_model;
    }

}