





import java.util.List;
import java.util.ArrayList;

public class core_SystemContext extends IdentifiedElement {






    private List<core_Variable> core_variables;




    private List<core_Actor> core_actors;


    public core_SystemContext(
    ) {
        super(
        );
        this.core_variables = new ArrayList<>();
        this.core_actors = new ArrayList<>();
    }

    public core_SystemContext(
        ArrayList<core_Variable> core_variables,        ArrayList<core_Actor> core_actors    ) {
        this.core_variables = core_variables;
        this.core_actors = core_actors;
    }


    public List<core_Variable> getCore_variables() {
        return core_variables;
    }

    public void addCore_variable(Core_variable core_variable) {
        this.core_variables.add(core_variable);
    }
    public List<core_Actor> getCore_actors() {
        return core_actors;
    }

    public void addCore_actor(Core_actor core_actor) {
        this.core_actors.add(core_actor);
    }

}