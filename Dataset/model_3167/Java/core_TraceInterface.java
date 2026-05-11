





import java.util.List;
import java.util.ArrayList;

public class core_TraceInterface extends ModuleDefinition {






    private List<core_TraceDefinition> core_tracedefinitions;


    public core_TraceInterface(
    ) {
        super(
        );
        this.core_tracedefinitions = new ArrayList<>();
    }

    public core_TraceInterface(
        ArrayList<core_TraceDefinition> core_tracedefinitions    ) {
        this.core_tracedefinitions = core_tracedefinitions;
    }


    public List<core_TraceDefinition> getCore_tracedefinitions() {
        return core_tracedefinitions;
    }

    public void addCore_tracedefinition(Core_tracedefinition core_tracedefinition) {
        this.core_tracedefinitions.add(core_tracedefinition);
    }

}