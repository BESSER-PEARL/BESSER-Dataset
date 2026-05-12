





import java.util.List;
import java.util.ArrayList;

public class core_SystemContext extends IdentifiedElement {






    private List<core_Variable> core_variables;




    private List<core_EObject> core_eobjects;




    private core_EObject core_eobject;


    public core_SystemContext(
    ) {
        super(
        );
        this.core_variables = new ArrayList<>();
        this.core_eobjects = new ArrayList<>();
    }

    public core_SystemContext(
        ArrayList<core_Variable> core_variables,        ArrayList<core_EObject> core_eobjects    ) {
        this.core_variables = core_variables;
        this.core_eobjects = core_eobjects;
    }


    public List<core_Variable> getCore_variables() {
        return core_variables;
    }

    public void addCore_variable(Core_variable core_variable) {
        this.core_variables.add(core_variable);
    }
    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }
    public core_EObject getCore_eobject() {
        return core_eobject;
    }

    public void setCore_eobject(core_EObject core_eobject) {
        this.core_eobject = core_eobject;
    }

}