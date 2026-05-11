





import java.util.List;
import java.util.ArrayList;

public class sWML_Class  {

    private String name;





    private sWML_IndexPage swml_indexpage;




    private sWML_ContentLayer swml_contentlayer;


    public sWML_Class(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sWML_IndexPage getSwml_indexpage() {
        return swml_indexpage;
    }

    public void setSwml_indexpage(sWML_IndexPage swml_indexpage) {
        this.swml_indexpage = swml_indexpage;
    }
    public sWML_ContentLayer getSwml_contentlayer() {
        return swml_contentlayer;
    }

    public void setSwml_contentlayer(sWML_ContentLayer swml_contentlayer) {
        this.swml_contentlayer = swml_contentlayer;
    }

}