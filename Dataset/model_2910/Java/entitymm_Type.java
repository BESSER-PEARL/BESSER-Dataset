





import java.util.List;
import java.util.ArrayList;

public class entitymm_Type  {

    private String name;





    private entitymm_Model entitymm_model;


    public entitymm_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entitymm_Model getEntitymm_model() {
        return entitymm_model;
    }

    public void setEntitymm_model(entitymm_Model entitymm_model) {
        this.entitymm_model = entitymm_model;
    }

}