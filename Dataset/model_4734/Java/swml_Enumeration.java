





import java.util.List;
import java.util.ArrayList;

public class swml_Enumeration  {

    private String name;





    private swml_ContentModel swml_contentmodel;


    public swml_Enumeration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_ContentModel getSwml_contentmodel() {
        return swml_contentmodel;
    }

    public void setSwml_contentmodel(swml_ContentModel swml_contentmodel) {
        this.swml_contentmodel = swml_contentmodel;
    }

}