





import java.util.List;
import java.util.ArrayList;

public class architectureTool_Port  {

    private String provided;
    private String simple;
    private String required;
    private String type;
    private String name;





    private List<architectureTool_Port> architecturetool_ports;


    public architectureTool_Port(
        String provided,        String simple,        String required,        String type,        String name    ) {
        this.provided = provided;
        this.simple = simple;
        this.required = required;
        this.type = type;
        this.name = name;
        this.architecturetool_ports = new ArrayList<>();
    }

    public architectureTool_Port(
        String provided,        String simple,        String required,        String type,        String name        ArrayList<architectureTool_Port> architecturetool_ports    ) {
        this.provided = provided;
        this.simple = simple;
        this.required = required;
        this.type = type;
        this.name = name;
        this.architecturetool_ports = architecturetool_ports;
    }

    public String getProvided() {
        return provided;
    }

    public void setProvided(String provided) {
        this.provided = provided;
    }
    public String getSimple() {
        return simple;
    }

    public void setSimple(String simple) {
        this.simple = simple;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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

}