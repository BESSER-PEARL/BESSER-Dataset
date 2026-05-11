





import java.util.List;
import java.util.ArrayList;

public class mDSL_Greeting  {

    private String name;





    private mDSL_Model mdsl_model;


    public mDSL_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mDSL_Model getMdsl_model() {
        return mdsl_model;
    }

    public void setMdsl_model(mDSL_Model mdsl_model) {
        this.mdsl_model = mdsl_model;
    }

}