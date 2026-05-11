





import java.util.List;
import java.util.ArrayList;

public class swml_Enumeration  {

    private String name;





    private swml_Attribute swml_attribute;




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

    public swml_Attribute getSwml_attribute() {
        return swml_attribute;
    }

    public void setSwml_attribute(swml_Attribute swml_attribute) {
        this.swml_attribute = swml_attribute;
    }
    public swml_ContentModel getSwml_contentmodel() {
        return swml_contentmodel;
    }

    public void setSwml_contentmodel(swml_ContentModel swml_contentmodel) {
        this.swml_contentmodel = swml_contentmodel;
    }

}