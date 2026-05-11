





import java.util.List;
import java.util.ArrayList;

public class classmodel_Import  {

    private String importURI;





    private classmodel_Model classmodel_model;


    public classmodel_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public classmodel_Model getClassmodel_model() {
        return classmodel_model;
    }

    public void setClassmodel_model(classmodel_Model classmodel_model) {
        this.classmodel_model = classmodel_model;
    }

}