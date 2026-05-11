





import java.util.List;
import java.util.ArrayList;

public class core_Requirement extends AbstractRequirement {






    private core_RequirementsContainer core_requirementscontainer;




    private core_RequirementsContainer core_requirementscontainer;




    private core_Requirement core_requirement;




    private List<core_Requirement> core_requirements;




    private core_RequirementsContainer core_requirementscontainer;


    public core_Requirement(
    ) {
        super(
        );
        this.core_requirements = new ArrayList<>();
    }

    public core_Requirement(
        ArrayList<core_Requirement> core_requirements    ) {
        this.core_requirements = core_requirements;
    }


    public core_RequirementsContainer getCore_requirementscontainer() {
        return core_requirementscontainer;
    }

    public void setCore_requirementscontainer(core_RequirementsContainer core_requirementscontainer) {
        this.core_requirementscontainer = core_requirementscontainer;
    }
    public core_RequirementsContainer getCore_requirementscontainer() {
        return core_requirementscontainer;
    }

    public void setCore_requirementscontainer(core_RequirementsContainer core_requirementscontainer) {
        this.core_requirementscontainer = core_requirementscontainer;
    }
    public core_Requirement getCore_requirement() {
        return core_requirement;
    }

    public void setCore_requirement(core_Requirement core_requirement) {
        this.core_requirement = core_requirement;
    }
    public List<core_Requirement> getCore_requirements() {
        return core_requirements;
    }

    public void addCore_requirement(Core_requirement core_requirement) {
        this.core_requirements.add(core_requirement);
    }
    public core_RequirementsContainer getCore_requirementscontainer() {
        return core_requirementscontainer;
    }

    public void setCore_requirementscontainer(core_RequirementsContainer core_requirementscontainer) {
        this.core_requirementscontainer = core_requirementscontainer;
    }

}