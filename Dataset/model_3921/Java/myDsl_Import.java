





import java.util.List;
import java.util.ArrayList;

public class myDsl_Import  {

    private String importURI;





    private myDsl_Model mydsl_model;


    public myDsl_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public myDsl_Model getMydsl_model() {
        return mydsl_model;
    }

    public void setMydsl_model(myDsl_Model mydsl_model) {
        this.mydsl_model = mydsl_model;
    }

}