





import java.util.List;
import java.util.ArrayList;

public class model_component_DeploymentNode extends UnicaseModelElement {






    private List<component_Component> component_components;


    public model_component_DeploymentNode(
    ) {
        super(
        );
        this.component_components = new ArrayList<>();
    }

    public model_component_DeploymentNode(
        ArrayList<component_Component> component_components    ) {
        this.component_components = component_components;
    }


    public List<component_Component> getComponent_components() {
        return component_components;
    }

    public void addComponent_component(Component_component component_component) {
        this.component_components.add(component_component);
    }

}