





import java.util.List;
import java.util.ArrayList;

public class requirements_editor_Person  {

    private String name;





    private List<requirements_editor_Requirement> requirements_editor_requirements;




    private requirements_editor_Requirement requirements_editor_requirement;


    public requirements_editor_Person(
        String name    ) {
        this.name = name;
        this.requirements_editor_requirements = new ArrayList<>();
    }

    public requirements_editor_Person(
        String name        ArrayList<requirements_editor_Requirement> requirements_editor_requirements    ) {
        this.name = name;
        this.requirements_editor_requirements = requirements_editor_requirements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<requirements_editor_Requirement> getRequirements_editor_requirements() {
        return requirements_editor_requirements;
    }

    public void addRequirements_editor_requirement(Requirements_editor_requirement requirements_editor_requirement) {
        this.requirements_editor_requirements.add(requirements_editor_requirement);
    }
    public requirements_editor_Requirement getRequirements_editor_requirement() {
        return requirements_editor_requirement;
    }

    public void setRequirements_editor_requirement(requirements_editor_Requirement requirements_editor_requirement) {
        this.requirements_editor_requirement = requirements_editor_requirement;
    }

}