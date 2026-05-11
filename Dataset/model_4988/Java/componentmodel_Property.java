





import java.util.List;
import java.util.ArrayList;

public class componentmodel_Property  {

    private String name;
    private String description;





    private componentmodel_PrimitiveComponent componentmodel_primitivecomponent;


    public componentmodel_Property(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public componentmodel_PrimitiveComponent getComponentmodel_primitivecomponent() {
        return componentmodel_primitivecomponent;
    }

    public void setComponentmodel_primitivecomponent(componentmodel_PrimitiveComponent componentmodel_primitivecomponent) {
        this.componentmodel_primitivecomponent = componentmodel_primitivecomponent;
    }

}