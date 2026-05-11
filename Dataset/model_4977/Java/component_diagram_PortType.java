





import java.util.List;
import java.util.ArrayList;

public class component_diagram_PortType extends IDBase {

    private String name;





    private component_diagram_PortInstance component_diagram_portinstance;




    private component_diagram_ComponentType component_diagram_componenttype;




    private component_diagram_ComponentType component_diagram_componenttype;




    private List<component_diagram_PortInstance> component_diagram_portinstances;


    public component_diagram_PortType(
        String name    ) {
        super(
        );
        this.name = name;
        this.component_diagram_portinstances = new ArrayList<>();
    }

    public component_diagram_PortType(
        String name        ArrayList<component_diagram_PortInstance> component_diagram_portinstances    ) {
        this.name = name;
        this.component_diagram_portinstances = component_diagram_portinstances;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public component_diagram_PortInstance getComponent_diagram_portinstance() {
        return component_diagram_portinstance;
    }

    public void setComponent_diagram_portinstance(component_diagram_PortInstance component_diagram_portinstance) {
        this.component_diagram_portinstance = component_diagram_portinstance;
    }
    public component_diagram_ComponentType getComponent_diagram_componenttype() {
        return component_diagram_componenttype;
    }

    public void setComponent_diagram_componenttype(component_diagram_ComponentType component_diagram_componenttype) {
        this.component_diagram_componenttype = component_diagram_componenttype;
    }
    public component_diagram_ComponentType getComponent_diagram_componenttype() {
        return component_diagram_componenttype;
    }

    public void setComponent_diagram_componenttype(component_diagram_ComponentType component_diagram_componenttype) {
        this.component_diagram_componenttype = component_diagram_componenttype;
    }
    public List<component_diagram_PortInstance> getComponent_diagram_portinstances() {
        return component_diagram_portinstances;
    }

    public void addComponent_diagram_portinstance(Component_diagram_portinstance component_diagram_portinstance) {
        this.component_diagram_portinstances.add(component_diagram_portinstance);
    }

}