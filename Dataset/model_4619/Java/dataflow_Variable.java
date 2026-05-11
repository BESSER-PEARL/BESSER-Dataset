





import java.util.List;
import java.util.ArrayList;

public class dataflow_Variable extends Attributable {

    private String name;
    private boolean shared;





    private dataflow_Actor dataflow_actor;




    private dataflow_Procedure dataflow_procedure;




    private dataflow_Actor dataflow_actor;


    public dataflow_Variable(
        String name,        boolean shared    ) {
        super(
        );
        this.name = name;
        this.shared = shared;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getShared() {
        return shared;
    }

    public void setShared(boolean shared) {
        this.shared = shared;
    }

    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }
    public dataflow_Procedure getDataflow_procedure() {
        return dataflow_procedure;
    }

    public void setDataflow_procedure(dataflow_Procedure dataflow_procedure) {
        this.dataflow_procedure = dataflow_procedure;
    }
    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }

}