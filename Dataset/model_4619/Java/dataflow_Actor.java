





import java.util.List;
import java.util.ArrayList;

public class dataflow_Actor extends Attributable {

    private String name;





    private dataflow_Actor dataflow_actor;




    private List<dataflow_Actor> dataflow_actors;


    public dataflow_Actor(
        String name    ) {
        super(
        );
        this.name = name;
        this.dataflow_actors = new ArrayList<>();
    }

    public dataflow_Actor(
        String name        ArrayList<dataflow_Actor> dataflow_actors    ) {
        this.name = name;
        this.dataflow_actors = dataflow_actors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }
    public List<dataflow_Actor> getDataflow_actors() {
        return dataflow_actors;
    }

    public void addDataflow_actor(Dataflow_actor dataflow_actor) {
        this.dataflow_actors.add(dataflow_actor);
    }

}