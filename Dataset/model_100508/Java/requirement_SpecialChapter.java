





import java.util.List;
import java.util.ArrayList;

public class requirement_SpecialChapter  {






    private requirement_RequirementProject requirement_requirementproject;




    private List<requirement_Requirement> requirement_requirements;




    private List<requirement_HierarchicalElement> requirement_hierarchicalelements;


    public requirement_SpecialChapter(
    ) {
        this.requirement_requirements = new ArrayList<>();
        this.requirement_hierarchicalelements = new ArrayList<>();
    }

    public requirement_SpecialChapter(
        ArrayList<requirement_Requirement> requirement_requirements,        ArrayList<requirement_HierarchicalElement> requirement_hierarchicalelements    ) {
        this.requirement_requirements = requirement_requirements;
        this.requirement_hierarchicalelements = requirement_hierarchicalelements;
    }


    public requirement_RequirementProject getRequirement_requirementproject() {
        return requirement_requirementproject;
    }

    public void setRequirement_requirementproject(requirement_RequirementProject requirement_requirementproject) {
        this.requirement_requirementproject = requirement_requirementproject;
    }
    public List<requirement_Requirement> getRequirement_requirements() {
        return requirement_requirements;
    }

    public void addRequirement_requirement(Requirement_requirement requirement_requirement) {
        this.requirement_requirements.add(requirement_requirement);
    }
    public List<requirement_HierarchicalElement> getRequirement_hierarchicalelements() {
        return requirement_hierarchicalelements;
    }

    public void addRequirement_hierarchicalelement(Requirement_hierarchicalelement requirement_hierarchicalelement) {
        this.requirement_hierarchicalelements.add(requirement_hierarchicalelement);
    }

}