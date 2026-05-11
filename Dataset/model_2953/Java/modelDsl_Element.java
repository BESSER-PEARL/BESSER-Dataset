





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Element  {

    private String name;





    private modelDsl_Model modeldsl_model;


    public modelDsl_Element(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public modelDsl_Model getModeldsl_model() {
        return modeldsl_model;
    }

    public void setModeldsl_model(modelDsl_Model modeldsl_model) {
        this.modeldsl_model = modeldsl_model;
    }

}