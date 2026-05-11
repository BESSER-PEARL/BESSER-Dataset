





import java.util.List;
import java.util.ArrayList;

public class swml_WebPage  {

    private String name;





    private swml_HypertextModel swml_hypertextmodel;


    public swml_WebPage(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_HypertextModel getSwml_hypertextmodel() {
        return swml_hypertextmodel;
    }

    public void setSwml_hypertextmodel(swml_HypertextModel swml_hypertextmodel) {
        this.swml_hypertextmodel = swml_hypertextmodel;
    }

}