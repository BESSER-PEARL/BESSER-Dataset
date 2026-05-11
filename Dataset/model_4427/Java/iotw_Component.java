





import java.util.List;
import java.util.ArrayList;

public class iotw_Component  {

    private String id;
    private String constraints;



    public iotw_Component(
        String id,        String constraints    ) {
        this.id = id;
        this.constraints = constraints;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getConstraints() {
        return constraints;
    }

    public void setConstraints(String constraints) {
        this.constraints = constraints;
    }


}