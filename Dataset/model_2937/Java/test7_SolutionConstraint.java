





import java.util.List;
import java.util.ArrayList;

public class test7_SolutionConstraint  {

    private String type;
    private String name;





    private test7_Model test7_model;


    public test7_SolutionConstraint(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public test7_Model getTest7_model() {
        return test7_model;
    }

    public void setTest7_model(test7_Model test7_model) {
        this.test7_model = test7_model;
    }

}