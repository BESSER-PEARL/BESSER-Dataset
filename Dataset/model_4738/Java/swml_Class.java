





import java.util.List;
import java.util.ArrayList;

public class swml_Class  {

    private String name;





    private swml_DynamicPage swml_dynamicpage;




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

    public swml_DynamicPage getSwml_dynamicpage() {
        return swml_dynamicpage;
    }

    public void setSwml_dynamicpage(swml_DynamicPage swml_dynamicpage) {
        this.swml_dynamicpage = swml_dynamicpage;
    }
    public swml_ContentLayer getSwml_contentlayer() {
        return swml_contentlayer;
    }

    public void setSwml_contentlayer(swml_ContentLayer swml_contentlayer) {
        this.swml_contentlayer = swml_contentlayer;
    }

}