





import java.util.List;
import java.util.ArrayList;

public class model_component_ComponentService extends UnicaseModelElement {






    private component_Component component_component;




    private List<component_Component> component_components;


    public model_component_ComponentService(
    ) {
        super(
        );
        this.component_components = new ArrayList<>();
    }

    public model_component_ComponentService(
        ArrayList<component_Component> component_components    ) {
        this.component_components = component_components;
    }


    public component_Component getComponent_component() {
        return component_component;
    }

    public void setComponent_component(component_Component component_component) {
        this.component_component = component_component;
    }
    public List<component_Component> getComponent_components() {
        return component_components;
    }

    public void addComponent_component(Component_component component_component) {
        this.component_components.add(component_component);
    }

}