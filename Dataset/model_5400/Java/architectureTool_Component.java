





import java.util.List;
import java.util.ArrayList;

public class architectureTool_Component  {

    private String name;





    private List<architectureTool_Port> architecturetool_ports;




    private List<architectureTool_Component> architecturetool_components;




    private List<architectureTool_Component> architecturetool_components;


    public architectureTool_Component(
        String name    ) {
        this.name = name;
        this.architecturetool_ports = new ArrayList<>();
        this.architecturetool_components = new ArrayList<>();
        this.architecturetool_components = new ArrayList<>();
    }

    public architectureTool_Component(
        String name        ArrayList<architectureTool_Port> architecturetool_ports,        ArrayList<architectureTool_Component> architecturetool_components,        ArrayList<architectureTool_Component> architecturetool_components    ) {
        this.name = name;
        this.architecturetool_ports = architecturetool_ports;
        this.architecturetool_components = architecturetool_components;
        this.architecturetool_components = architecturetool_components;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public List<architectureTool_Component> getArchitecturetool_components() {
        return architecturetool_components;
    }

    public void addArchitecturetool_component(Architecturetool_component architecturetool_component) {
        this.architecturetool_components.add(architecturetool_component);
    }

}