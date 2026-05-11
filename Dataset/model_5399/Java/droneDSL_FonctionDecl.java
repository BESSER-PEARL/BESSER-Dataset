





import java.util.List;
import java.util.ArrayList;

public class droneDSL_FonctionDecl  {

    private String name;





    private droneDSL_Model dronedsl_model;


    public droneDSL_FonctionDecl(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public droneDSL_Model getDronedsl_model() {
        return dronedsl_model;
    }

    public void setDronedsl_model(droneDSL_Model dronedsl_model) {
        this.dronedsl_model = dronedsl_model;
    }

}