





import java.util.List;
import java.util.ArrayList;

public class swml_EntityType  {

    private String name;
    private boolean isAbstract;





    private swml_EntityType swml_entitytype;




    private swml_ContentModel swml_contentmodel;


    public swml_EntityType(
        String name,        boolean isAbstract    ) {
        this.name = name;
        this.isAbstract = isAbstract;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public swml_EntityType getSwml_entitytype() {
        return swml_entitytype;
    }

    public void setSwml_entitytype(swml_EntityType swml_entitytype) {
        this.swml_entitytype = swml_entitytype;
    }
    public swml_ContentModel getSwml_contentmodel() {
        return swml_contentmodel;
    }

    public void setSwml_contentmodel(swml_ContentModel swml_contentmodel) {
        this.swml_contentmodel = swml_contentmodel;
    }

}