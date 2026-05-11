





import java.util.List;
import java.util.ArrayList;

public class component_diagram_Architecture extends IDBase {






    private List<component_diagram_ComponentType> component_diagram_componenttypes;




    private List<component_diagram_ComponentInstance> component_diagram_componentinstances;




    private List<component_diagram_PortType> component_diagram_porttypes;




    private List<component_diagram_Connector> component_diagram_connectors;




    private List<component_diagram_PortInstance> component_diagram_portinstances;


    public component_diagram_Architecture(
    ) {
        super(
        );
        this.component_diagram_componenttypes = new ArrayList<>();
        this.component_diagram_componentinstances = new ArrayList<>();
        this.component_diagram_porttypes = new ArrayList<>();
        this.component_diagram_connectors = new ArrayList<>();
        this.component_diagram_portinstances = new ArrayList<>();
    }

    public component_diagram_Architecture(
        ArrayList<component_diagram_ComponentType> component_diagram_componenttypes,        ArrayList<component_diagram_ComponentInstance> component_diagram_componentinstances,        ArrayList<component_diagram_PortType> component_diagram_porttypes,        ArrayList<component_diagram_Connector> component_diagram_connectors,        ArrayList<component_diagram_PortInstance> component_diagram_portinstances    ) {
        this.component_diagram_componenttypes = component_diagram_componenttypes;
        this.component_diagram_componentinstances = component_diagram_componentinstances;
        this.component_diagram_porttypes = component_diagram_porttypes;
        this.component_diagram_connectors = component_diagram_connectors;
        this.component_diagram_portinstances = component_diagram_portinstances;
    }


    public List<component_diagram_ComponentType> getComponent_diagram_componenttypes() {
        return component_diagram_componenttypes;
    }

    public void addComponent_diagram_componenttype(Component_diagram_componenttype component_diagram_componenttype) {
        this.component_diagram_componenttypes.add(component_diagram_componenttype);
    }
    public List<component_diagram_ComponentInstance> getComponent_diagram_componentinstances() {
        return component_diagram_componentinstances;
    }

    public void addComponent_diagram_componentinstance(Component_diagram_componentinstance component_diagram_componentinstance) {
        this.component_diagram_componentinstances.add(component_diagram_componentinstance);
    }
    public List<component_diagram_PortType> getComponent_diagram_porttypes() {
        return component_diagram_porttypes;
    }

    public void addComponent_diagram_porttype(Component_diagram_porttype component_diagram_porttype) {
        this.component_diagram_porttypes.add(component_diagram_porttype);
    }
    public List<component_diagram_Connector> getComponent_diagram_connectors() {
        return component_diagram_connectors;
    }

    public void addComponent_diagram_connector(Component_diagram_connector component_diagram_connector) {
        this.component_diagram_connectors.add(component_diagram_connector);
    }
    public List<component_diagram_PortInstance> getComponent_diagram_portinstances() {
        return component_diagram_portinstances;
    }

    public void addComponent_diagram_portinstance(Component_diagram_portinstance component_diagram_portinstance) {
        this.component_diagram_portinstances.add(component_diagram_portinstance);
    }

}