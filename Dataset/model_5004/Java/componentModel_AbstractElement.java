





import java.util.List;
import java.util.ArrayList;

public class componentModel_AbstractElement  {

    private String name;





    private componentModel_ComponentModel componentmodel_componentmodel;


    public componentModel_AbstractElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentModel_ComponentModel getComponentmodel_componentmodel() {
        return componentmodel_componentmodel;
    }

    public void setComponentmodel_componentmodel(componentModel_ComponentModel componentmodel_componentmodel) {
        this.componentmodel_componentmodel = componentmodel_componentmodel;
    }

}