





import java.util.List;
import java.util.ArrayList;

public class componentmodel_CompositeComponent extends Component {






    private List<componentmodel_Component> componentmodel_components;


    public componentmodel_CompositeComponent(
    ) {
        super(
        );
        this.componentmodel_components = new ArrayList<>();
    }

    public componentmodel_CompositeComponent(
        ArrayList<componentmodel_Component> componentmodel_components    ) {
        this.componentmodel_components = componentmodel_components;
    }


    public List<componentmodel_Component> getComponentmodel_components() {
        return componentmodel_components;
    }

    public void addComponentmodel_component(Componentmodel_component componentmodel_component) {
        this.componentmodel_components.add(componentmodel_component);
    }

}