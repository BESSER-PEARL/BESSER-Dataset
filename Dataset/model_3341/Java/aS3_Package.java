





import java.util.List;
import java.util.ArrayList;

public class aS3_Package  {

    private String name;





    private aS3_Model as3_model;


    public aS3_Package(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aS3_Model getAs3_model() {
        return as3_model;
    }

    public void setAs3_model(aS3_Model as3_model) {
        this.as3_model = as3_model;
    }

}