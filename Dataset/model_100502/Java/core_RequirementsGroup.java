





import java.util.List;
import java.util.ArrayList;

public class core_RequirementsGroup extends VerifiableElement {






    private core_Specification core_specification;




    private core_Specification core_specification;




    private List<core_AbstractRequirement> core_abstractrequirements;




    private core_AbstractRequirement core_abstractrequirement;


    public core_RequirementsGroup(
    ) {
        super(
        );
        this.core_abstractrequirements = new ArrayList<>();
    }

    public core_RequirementsGroup(
        ArrayList<core_AbstractRequirement> core_abstractrequirements    ) {
        this.core_abstractrequirements = core_abstractrequirements;
    }


    public core_Specification getCore_specification() {
        return core_specification;
    }

    public void setCore_specification(core_Specification core_specification) {
        this.core_specification = core_specification;
    }
    public core_Specification getCore_specification() {
        return core_specification;
    }

    public void setCore_specification(core_Specification core_specification) {
        this.core_specification = core_specification;
    }
    public List<core_AbstractRequirement> getCore_abstractrequirements() {
        return core_abstractrequirements;
    }

    public void addCore_abstractrequirement(Core_abstractrequirement core_abstractrequirement) {
        this.core_abstractrequirements.add(core_abstractrequirement);
    }
    public core_AbstractRequirement getCore_abstractrequirement() {
        return core_abstractrequirement;
    }

    public void setCore_abstractrequirement(core_AbstractRequirement core_abstractrequirement) {
        this.core_abstractrequirement = core_abstractrequirement;
    }

}