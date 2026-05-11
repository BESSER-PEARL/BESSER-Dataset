





import java.util.List;
import java.util.ArrayList;

public class architectureTool_Interface extends classMember {






    private List<architectureTool_Class> architecturetool_classs;




    private architectureTool_Interface architecturetool_interface;




    private List<architectureTool_Port> architecturetool_ports;




    private architectureTool_Class architecturetool_class;




    private List<architectureTool_Port> architecturetool_ports;




    private architectureTool_Component architecturetool_component;




    private architectureTool_Port architecturetool_port;




    private architectureTool_Port architecturetool_port;


    public architectureTool_Interface(
    ) {
        super(
        );
        this.architecturetool_classs = new ArrayList<>();
        this.architecturetool_ports = new ArrayList<>();
        this.architecturetool_ports = new ArrayList<>();
    }

    public architectureTool_Interface(
        ArrayList<architectureTool_Class> architecturetool_classs,        ArrayList<architectureTool_Port> architecturetool_ports,        ArrayList<architectureTool_Port> architecturetool_ports    ) {
        this.architecturetool_classs = architecturetool_classs;
        this.architecturetool_ports = architecturetool_ports;
        this.architecturetool_ports = architecturetool_ports;
    }


    public List<architectureTool_Class> getArchitecturetool_classs() {
        return architecturetool_classs;
    }

    public void addArchitecturetool_class(Architecturetool_class architecturetool_class) {
        this.architecturetool_classs.add(architecturetool_class);
    }
    public architectureTool_Interface getArchitecturetool_interface() {
        return architecturetool_interface;
    }

    public void setArchitecturetool_interface(architectureTool_Interface architecturetool_interface) {
        this.architecturetool_interface = architecturetool_interface;
    }
    public List<architectureTool_Port> getArchitecturetool_ports() {
        return architecturetool_ports;
    }

    public void addArchitecturetool_port(Architecturetool_port architecturetool_port) {
        this.architecturetool_ports.add(architecturetool_port);
    }
    public architectureTool_Class getArchitecturetool_class() {
        return architecturetool_class;
    }

    public void setArchitecturetool_class(architectureTool_Class architecturetool_class) {
        this.architecturetool_class = architecturetool_class;
    }
    public List<architectureTool_Port> getArchitecturetool_ports() {
        return architecturetool_ports;
    }

    public void addArchitecturetool_port(Architecturetool_port architecturetool_port) {
        this.architecturetool_ports.add(architecturetool_port);
    }
    public architectureTool_Component getArchitecturetool_component() {
        return architecturetool_component;
    }

    public void setArchitecturetool_component(architectureTool_Component architecturetool_component) {
        this.architecturetool_component = architecturetool_component;
    }
    public architectureTool_Port getArchitecturetool_port() {
        return architecturetool_port;
    }

    public void setArchitecturetool_port(architectureTool_Port architecturetool_port) {
        this.architecturetool_port = architecturetool_port;
    }
    public architectureTool_Port getArchitecturetool_port() {
        return architecturetool_port;
    }

    public void setArchitecturetool_port(architectureTool_Port architecturetool_port) {
        this.architecturetool_port = architecturetool_port;
    }

}