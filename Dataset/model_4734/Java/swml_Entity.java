





import java.util.List;
import java.util.ArrayList;

public class swml_Entity  {

    private String name;





    private swml_Entity swml_entity;




    private swml_ContentModel swml_contentmodel;


    public swml_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_Entity getSwml_entity() {
        return swml_entity;
    }

    public void setSwml_entity(swml_Entity swml_entity) {
        this.swml_entity = swml_entity;
    }
    public swml_ContentModel getSwml_contentmodel() {
        return swml_contentmodel;
    }

    public void setSwml_contentmodel(swml_ContentModel swml_contentmodel) {
        this.swml_contentmodel = swml_contentmodel;
    }

}