





import java.util.List;
import java.util.ArrayList;

public class component_diagram_ComponentInstance extends IDBase {

    private int version;
    private String name;





    private component_diagram_ComponentType component_diagram_componenttype;




    private List<component_diagram_PortInstance> component_diagram_portinstances;




    private component_diagram_ComponentInstance component_diagram_componentinstance;




    private component_diagram_PortInstance component_diagram_portinstance;




    private List<component_diagram_PortInstance> component_diagram_portinstances;




    private component_diagram_ComponentType component_diagram_componenttype;




    private List<component_diagram_ComponentInstance> component_diagram_componentinstances;




    private component_diagram_PortInstance component_diagram_portinstance;


    public component_diagram_ComponentInstance(
        int version,        String name    ) {
        super(
        );
        this.version = version;
        this.name = name;
        this.component_diagram_portinstances = new ArrayList<>();
        this.component_diagram_portinstances = new ArrayList<>();
        this.component_diagram_componentinstances = new ArrayList<>();
    }

    public component_diagram_ComponentInstance(
        int version,        String name        ArrayList<component_diagram_PortInstance> component_diagram_portinstances,        ArrayList<component_diagram_PortInstance> component_diagram_portinstances,        ArrayList<component_diagram_ComponentInstance> component_diagram_componentinstances    ) {
        this.version = version;
        this.name = name;
        this.component_diagram_portinstances = component_diagram_portinstances;
        this.component_diagram_portinstances = component_diagram_portinstances;
        this.component_diagram_componentinstances = component_diagram_componentinstances;
    }

    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public component_diagram_ComponentInstance getComponent_diagram_componentinstance() {
        return component_diagram_componentinstance;
    }

    public void setComponent_diagram_componentinstance(component_diagram_ComponentInstance component_diagram_componentinstance) {
        this.component_diagram_componentinstance = component_diagram_componentinstance;
    }
    public component_diagram_PortInstance getComponent_diagram_portinstance() {
        return component_diagram_portinstance;
    }

    public void setComponent_diagram_portinstance(component_diagram_PortInstance component_diagram_portinstance) {
        this.component_diagram_portinstance = component_diagram_portinstance;
    }
    public List<component_diagram_PortInstance> getComponent_diagram_portinstances() {
        return component_diagram_portinstances;
    }

    public void addComponent_diagram_portinstance(Component_diagram_portinstance component_diagram_portinstance) {
        this.component_diagram_portinstances.add(component_diagram_portinstance);
    }
    public component_diagram_ComponentType getComponent_diagram_componenttype() {
        return component_diagram_componenttype;
    }

    public void setComponent_diagram_componenttype(component_diagram_ComponentType component_diagram_componenttype) {
        this.component_diagram_componenttype = component_diagram_componenttype;
    }
    public List<component_diagram_ComponentInstance> getComponent_diagram_componentinstances() {
        return component_diagram_componentinstances;
    }

    public void addComponent_diagram_componentinstance(Component_diagram_componentinstance component_diagram_componentinstance) {
        this.component_diagram_componentinstances.add(component_diagram_componentinstance);
    }
    public component_diagram_PortInstance getComponent_diagram_portinstance() {
        return component_diagram_portinstance;
    }

    public void setComponent_diagram_portinstance(component_diagram_PortInstance component_diagram_portinstance) {
        this.component_diagram_portinstance = component_diagram_portinstance;
    }

}