





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_ModelElement  {

    private String name;





    private applauseDsl_Model applausedsl_model;


    public applauseDsl_ModelElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public applauseDsl_Model getApplausedsl_model() {
        return applausedsl_model;
    }

    public void setApplausedsl_model(applauseDsl_Model applausedsl_model) {
        this.applausedsl_model = applausedsl_model;
    }

}