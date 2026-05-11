





import java.util.List;
import java.util.ArrayList;

public class componentmodel_Port  {

    private String name;
    private String type;
    private String typePackage;
    private String description;





    private componentmodel_Component componentmodel_component;


    public componentmodel_Port(
        String name,        String type,        String typePackage,        String description    ) {
        this.name = name;
        this.type = type;
        this.typePackage = typePackage;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTypepackage() {
        return typePackage;
    }

    public void setTypepackage(String typePackage) {
        this.typePackage = typePackage;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public componentmodel_Component getComponentmodel_component() {
        return componentmodel_component;
    }

    public void setComponentmodel_component(componentmodel_Component componentmodel_component) {
        this.componentmodel_component = componentmodel_component;
    }

}