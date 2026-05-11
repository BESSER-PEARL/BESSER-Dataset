





import java.util.List;
import java.util.ArrayList;

public class adfg_Actor  {

    private int nbPorts;
    private String sourceCode;
    private String name;
    private int procNumber;
    private int priority;





    private adfg_Port adfg_port;




    private adfg_Graph adfg_graph;




    private List<adfg_Port> adfg_ports;




    private adfg_Graph adfg_graph;


    public adfg_Actor(
        int nbPorts,        String sourceCode,        String name,        int procNumber,        int priority    ) {
        this.nbPorts = nbPorts;
        this.sourceCode = sourceCode;
        this.name = name;
        this.procNumber = procNumber;
        this.priority = priority;
        this.adfg_ports = new ArrayList<>();
    }

    public adfg_Actor(
        int nbPorts,        String sourceCode,        String name,        int procNumber,        int priority        ArrayList<adfg_Port> adfg_ports    ) {
        this.nbPorts = nbPorts;
        this.sourceCode = sourceCode;
        this.name = name;
        this.procNumber = procNumber;
        this.priority = priority;
        this.adfg_ports = adfg_ports;
    }

    public int getNbports() {
        return nbPorts;
    }

    public void setNbports(int nbPorts) {
        this.nbPorts = nbPorts;
    }
    public String getSourcecode() {
        return sourceCode;
    }

    public void setSourcecode(String sourceCode) {
        this.sourceCode = sourceCode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getProcnumber() {
        return procNumber;
    }

    public void setProcnumber(int procNumber) {
        this.procNumber = procNumber;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public adfg_Port getAdfg_port() {
        return adfg_port;
    }

    public void setAdfg_port(adfg_Port adfg_port) {
        this.adfg_port = adfg_port;
    }
    public adfg_Graph getAdfg_graph() {
        return adfg_graph;
    }

    public void setAdfg_graph(adfg_Graph adfg_graph) {
        this.adfg_graph = adfg_graph;
    }
    public List<adfg_Port> getAdfg_ports() {
        return adfg_ports;
    }

    public void addAdfg_port(Adfg_port adfg_port) {
        this.adfg_ports.add(adfg_port);
    }
    public adfg_Graph getAdfg_graph() {
        return adfg_graph;
    }

    public void setAdfg_graph(adfg_Graph adfg_graph) {
        this.adfg_graph = adfg_graph;
    }

}