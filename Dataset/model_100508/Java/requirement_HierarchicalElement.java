





import java.util.List;
import java.util.ArrayList;

public class requirement_HierarchicalElement extends IdentifiedElement {

    private String nextReqIndex;





    private requirement_HierarchicalElement requirement_hierarchicalelement;




    private requirement_RequirementProject requirement_requirementproject;




    private requirement_HierarchicalElement requirement_hierarchicalelement;




    private List<requirement_Requirement> requirement_requirements;


    public requirement_HierarchicalElement(
        String nextReqIndex    ) {
        super(
        );
        this.nextReqIndex = nextReqIndex;
        this.requirement_requirements = new ArrayList<>();
    }

    public requirement_HierarchicalElement(
        String nextReqIndex        ArrayList<requirement_Requirement> requirement_requirements    ) {
        this.nextReqIndex = nextReqIndex;
        this.requirement_requirements = requirement_requirements;
    }

    public String getNextreqindex() {
        return nextReqIndex;
    }

    public void setNextreqindex(String nextReqIndex) {
        this.nextReqIndex = nextReqIndex;
    }

    public requirement_HierarchicalElement getRequirement_hierarchicalelement() {
        return requirement_hierarchicalelement;
    }

    public void setRequirement_hierarchicalelement(requirement_HierarchicalElement requirement_hierarchicalelement) {
        this.requirement_hierarchicalelement = requirement_hierarchicalelement;
    }
    public requirement_RequirementProject getRequirement_requirementproject() {
        return requirement_requirementproject;
    }

    public void setRequirement_requirementproject(requirement_RequirementProject requirement_requirementproject) {
        this.requirement_requirementproject = requirement_requirementproject;
    }
    public requirement_HierarchicalElement getRequirement_hierarchicalelement() {
        return requirement_hierarchicalelement;
    }

    public void setRequirement_hierarchicalelement(requirement_HierarchicalElement requirement_hierarchicalelement) {
        this.requirement_hierarchicalelement = requirement_hierarchicalelement;
    }
    public List<requirement_Requirement> getRequirement_requirements() {
        return requirement_requirements;
    }

    public void addRequirement_requirement(Requirement_requirement requirement_requirement) {
        this.requirement_requirements.add(requirement_requirement);
    }

}