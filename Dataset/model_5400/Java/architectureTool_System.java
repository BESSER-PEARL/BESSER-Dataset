





import java.util.List;
import java.util.ArrayList;

public class architectureTool_System  {

    private String name;





    private List<architectureTool_System> architecturetool_systems;




    private List<architectureTool_System> architecturetool_systems;




    private List<architectureTool_Component> architecturetool_components;




    private List<architectureTool_Interface> architecturetool_interfaces;




    private architectureTool_Component architecturetool_component;




    private List<architectureTool_Port> architecturetool_ports;




    private List<architectureTool_Component> architecturetool_components;


    public architectureTool_System(
        String name    ) {
        this.name = name;
        this.architecturetool_systems = new ArrayList<>();
        this.architecturetool_systems = new ArrayList<>();
        this.architecturetool_components = new ArrayList<>();
        this.architecturetool_interfaces = new ArrayList<>();
        this.architecturetool_ports = new ArrayList<>();
        this.architecturetool_components = new ArrayList<>();
    }

    public architectureTool_System(
        String name        ArrayList<architectureTool_System> architecturetool_systems,        ArrayList<architectureTool_System> architecturetool_systems,        ArrayList<architectureTool_Component> architecturetool_components,        ArrayList<architectureTool_Interface> architecturetool_interfaces,        ArrayList<architectureTool_Port> architecturetool_ports,        ArrayList<architectureTool_Component> architecturetool_components    ) {
        this.name = name;
        this.architecturetool_systems = architecturetool_systems;
        this.architecturetool_systems = architecturetool_systems;
        this.architecturetool_components = architecturetool_components;
        this.architecturetool_interfaces = architecturetool_interfaces;
        this.architecturetool_ports = architecturetool_ports;
        this.architecturetool_components = architecturetool_components;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<architectureTool_System> getArchitecturetool_systems() {
        return architecturetool_systems;
    }

    public void addArchitecturetool_system(Architecturetool_system architecturetool_system) {
        this.architecturetool_systems.add(architecturetool_system);
    }
    public List<architectureTool_System> getArchitecturetool_systems() {
        return architecturetool_systems;
    }

    public void addArchitecturetool_system(Architecturetool_system architecturetool_system) {
        this.architecturetool_systems.add(architecturetool_system);
    }
    public List<architectureTool_Component> getArchitecturetool_components() {
        return architecturetool_components;
    }

    public void addArchitecturetool_component(Architecturetool_component architecturetool_component) {
        this.architecturetool_components.add(architecturetool_component);
    }
    public List<architectureTool_Interface> getArchitecturetool_interfaces() {
        return architecturetool_interfaces;
    }

    public void addArchitecturetool_interface(Architecturetool_interface architecturetool_interface) {
        this.architecturetool_interfaces.add(architecturetool_interface);
    }
    public architectureTool_Component getArchitecturetool_component() {
        return architecturetool_component;
    }

    public void setArchitecturetool_component(architectureTool_Component architecturetool_component) {
        this.architecturetool_component = architecturetool_component;
    }
    public List<architectureTool_Port> getArchitecturetool_ports() {
        return architecturetool_ports;
    }

    public void addArchitecturetool_port(Architecturetool_port architecturetool_port) {
        this.architecturetool_ports.add(architecturetool_port);
    }
    public List<architectureTool_Component> getArchitecturetool_components() {
        return architecturetool_components;
    }

    public void addArchitecturetool_component(Architecturetool_component architecturetool_component) {
        this.architecturetool_components.add(architecturetool_component);
    }

}