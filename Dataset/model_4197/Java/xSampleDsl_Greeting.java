





import java.util.List;
import java.util.ArrayList;

public class xSampleDsl_Greeting  {

    private String name;





    private xSampleDsl_Model xsampledsl_model;


    public xSampleDsl_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xSampleDsl_Model getXsampledsl_model() {
        return xsampledsl_model;
    }

    public void setXsampledsl_model(xSampleDsl_Model xsampledsl_model) {
        this.xsampledsl_model = xsampledsl_model;
    }

}