





import java.util.List;
import java.util.ArrayList;

public class swml_WebModel  {

    private String name;





    private swml_ContentLayer swml_contentlayer;




    private swml_HypertextLayer swml_hypertextlayer;


    public swml_WebModel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_ContentLayer getSwml_contentlayer() {
        return swml_contentlayer;
    }

    public void setSwml_contentlayer(swml_ContentLayer swml_contentlayer) {
        this.swml_contentlayer = swml_contentlayer;
    }
    public swml_HypertextLayer getSwml_hypertextlayer() {
        return swml_hypertextlayer;
    }

    public void setSwml_hypertextlayer(swml_HypertextLayer swml_hypertextlayer) {
        this.swml_hypertextlayer = swml_hypertextlayer;
    }

}