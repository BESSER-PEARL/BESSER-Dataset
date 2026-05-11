





import java.util.List;
import java.util.ArrayList;

public class swml_v2_Class  {

    private String name;





    private swml_v2_ContentLayer swml_v2_contentlayer;


    public swml_v2_Class(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_v2_ContentLayer getSwml_v2_contentlayer() {
        return swml_v2_contentlayer;
    }

    public void setSwml_v2_contentlayer(swml_v2_ContentLayer swml_v2_contentlayer) {
        this.swml_v2_contentlayer = swml_v2_contentlayer;
    }

}