





import java.util.List;
import java.util.ArrayList;

public class frontend_core_TraceInterface extends ModuleDefinition {






    private List<TraceDefinition> tracedefinitions;


    public frontend_core_TraceInterface(
    ) {
        super(
        );
        this.tracedefinitions = new ArrayList<>();
    }

    public frontend_core_TraceInterface(
        ArrayList<TraceDefinition> tracedefinitions    ) {
        this.tracedefinitions = tracedefinitions;
    }


    public List<TraceDefinition> getTracedefinitions() {
        return tracedefinitions;
    }

    public void addTracedefinition(Tracedefinition tracedefinition) {
        this.tracedefinitions.add(tracedefinition);
    }

}