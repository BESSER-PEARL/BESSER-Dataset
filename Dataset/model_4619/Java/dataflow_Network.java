





import java.util.List;
import java.util.ArrayList;

public class dataflow_Network extends Attributable {

    private String sourceFile;
    private String name;
    private String project;





    private List<dataflow_Port> dataflow_ports;




    private dataflow_ActorClass dataflow_actorclass;




    private List<dataflow_Actor> dataflow_actors;




    private dataflow_Buffer dataflow_buffer;




    private List<dataflow_ActorClass> dataflow_actorclasss;




    private List<dataflow_Port> dataflow_ports;




    private dataflow_Actor dataflow_actor;




    private List<dataflow_SharedVariable> dataflow_sharedvariables;




    private List<dataflow_Buffer> dataflow_buffers;


    public dataflow_Network(
        String sourceFile,        String name,        String project    ) {
        super(
        );
        this.sourceFile = sourceFile;
        this.name = name;
        this.project = project;
        this.dataflow_ports = new ArrayList<>();
        this.dataflow_actors = new ArrayList<>();
        this.dataflow_actorclasss = new ArrayList<>();
        this.dataflow_ports = new ArrayList<>();
        this.dataflow_sharedvariables = new ArrayList<>();
        this.dataflow_buffers = new ArrayList<>();
    }

    public dataflow_Network(
        String sourceFile,        String name,        String project        ArrayList<dataflow_Port> dataflow_ports,        ArrayList<dataflow_Actor> dataflow_actors,        ArrayList<dataflow_ActorClass> dataflow_actorclasss,        ArrayList<dataflow_Port> dataflow_ports,        ArrayList<dataflow_SharedVariable> dataflow_sharedvariables,        ArrayList<dataflow_Buffer> dataflow_buffers    ) {
        this.sourceFile = sourceFile;
        this.name = name;
        this.project = project;
        this.dataflow_ports = dataflow_ports;
        this.dataflow_actors = dataflow_actors;
        this.dataflow_actorclasss = dataflow_actorclasss;
        this.dataflow_ports = dataflow_ports;
        this.dataflow_sharedvariables = dataflow_sharedvariables;
        this.dataflow_buffers = dataflow_buffers;
    }

    public String getSourcefile() {
        return sourceFile;
    }

    public void setSourcefile(String sourceFile) {
        this.sourceFile = sourceFile;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }

    public List<dataflow_Port> getDataflow_ports() {
        return dataflow_ports;
    }

    public void addDataflow_port(Dataflow_port dataflow_port) {
        this.dataflow_ports.add(dataflow_port);
    }
    public dataflow_ActorClass getDataflow_actorclass() {
        return dataflow_actorclass;
    }

    public void setDataflow_actorclass(dataflow_ActorClass dataflow_actorclass) {
        this.dataflow_actorclass = dataflow_actorclass;
    }
    public List<dataflow_Actor> getDataflow_actors() {
        return dataflow_actors;
    }

    public void addDataflow_actor(Dataflow_actor dataflow_actor) {
        this.dataflow_actors.add(dataflow_actor);
    }
    public dataflow_Buffer getDataflow_buffer() {
        return dataflow_buffer;
    }

    public void setDataflow_buffer(dataflow_Buffer dataflow_buffer) {
        this.dataflow_buffer = dataflow_buffer;
    }
    public List<dataflow_ActorClass> getDataflow_actorclasss() {
        return dataflow_actorclasss;
    }

    public void addDataflow_actorclass(Dataflow_actorclass dataflow_actorclass) {
        this.dataflow_actorclasss.add(dataflow_actorclass);
    }
    public List<dataflow_Port> getDataflow_ports() {
        return dataflow_ports;
    }

    public void addDataflow_port(Dataflow_port dataflow_port) {
        this.dataflow_ports.add(dataflow_port);
    }
    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }
    public List<dataflow_SharedVariable> getDataflow_sharedvariables() {
        return dataflow_sharedvariables;
    }

    public void addDataflow_sharedvariable(Dataflow_sharedvariable dataflow_sharedvariable) {
        this.dataflow_sharedvariables.add(dataflow_sharedvariable);
    }
    public List<dataflow_Buffer> getDataflow_buffers() {
        return dataflow_buffers;
    }

    public void addDataflow_buffer(Dataflow_buffer dataflow_buffer) {
        this.dataflow_buffers.add(dataflow_buffer);
    }

}