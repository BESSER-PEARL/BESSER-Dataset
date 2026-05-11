





import java.util.List;
import java.util.ArrayList;

public class swml_Class  {

    private String name;





    private swml_ContentLayer swml_contentlayer;


    public swml_Class(
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

}