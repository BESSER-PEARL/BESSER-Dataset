





import java.util.List;
import java.util.ArrayList;

public class componentModel_AssemblyContext extends AssemblyViewType {

    private String name;





    private componentModel_Component componentmodel_component;


    public componentModel_AssemblyContext(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentModel_Component getComponentmodel_component() {
        return componentmodel_component;
    }

    public void setComponentmodel_component(componentModel_Component componentmodel_component) {
        this.componentmodel_component = componentmodel_component;
    }

}