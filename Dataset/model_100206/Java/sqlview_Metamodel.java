





import java.util.List;
import java.util.ArrayList;

public class sqlview_Metamodel  {

    private String metamodelURL;





    private sqlview_Model sqlview_model;


    public sqlview_Metamodel(
        String metamodelURL    ) {
        this.metamodelURL = metamodelURL;
    }


    public String getMetamodelurl() {
        return metamodelURL;
    }

    public void setMetamodelurl(String metamodelURL) {
        this.metamodelURL = metamodelURL;
    }

    public sqlview_Model getSqlview_model() {
        return sqlview_model;
    }

    public void setSqlview_model(sqlview_Model sqlview_model) {
        this.sqlview_model = sqlview_model;
    }

}