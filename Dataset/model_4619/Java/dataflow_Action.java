





import java.util.List;
import java.util.ArrayList;

public class dataflow_Action extends Attributable {

    private String name;





    private List<dataflow_Port> dataflow_ports;




    private List<dataflow_Port> dataflow_ports;




    private List<dataflow_Guard> dataflow_guards;




    private dataflow_Actor dataflow_actor;




    private dataflow_Guard dataflow_guard;




    private dataflow_Port dataflow_port;




    private dataflow_Port dataflow_port;




    private dataflow_Actor dataflow_actor;


    public dataflow_Action(
        String name    ) {
        super(
        );
        this.name = name;
        this.dataflow_ports = new ArrayList<>();
        this.dataflow_ports = new ArrayList<>();
        this.dataflow_guards = new ArrayList<>();
    }

    public dataflow_Action(
        String name        ArrayList<dataflow_Port> dataflow_ports,        ArrayList<dataflow_Port> dataflow_ports,        ArrayList<dataflow_Guard> dataflow_guards    ) {
        this.name = name;
        this.dataflow_ports = dataflow_ports;
        this.dataflow_ports = dataflow_ports;
        this.dataflow_guards = dataflow_guards;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<dataflow_Port> getDataflow_ports() {
        return dataflow_ports;
    }

    public void addDataflow_port(Dataflow_port dataflow_port) {
        this.dataflow_ports.add(dataflow_port);
    }
    public List<dataflow_Port> getDataflow_ports() {
        return dataflow_ports;
    }

    public void addDataflow_port(Dataflow_port dataflow_port) {
        this.dataflow_ports.add(dataflow_port);
    }
    public List<dataflow_Guard> getDataflow_guards() {
        return dataflow_guards;
    }

    public void addDataflow_guard(Dataflow_guard dataflow_guard) {
        this.dataflow_guards.add(dataflow_guard);
    }
    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }
    public dataflow_Guard getDataflow_guard() {
        return dataflow_guard;
    }

    public void setDataflow_guard(dataflow_Guard dataflow_guard) {
        this.dataflow_guard = dataflow_guard;
    }
    public dataflow_Port getDataflow_port() {
        return dataflow_port;
    }

    public void setDataflow_port(dataflow_Port dataflow_port) {
        this.dataflow_port = dataflow_port;
    }
    public dataflow_Port getDataflow_port() {
        return dataflow_port;
    }

    public void setDataflow_port(dataflow_Port dataflow_port) {
        this.dataflow_port = dataflow_port;
    }
    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }

}