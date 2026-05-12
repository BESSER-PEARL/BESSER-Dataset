





import java.util.List;
import java.util.ArrayList;

public class requirement_Category extends NamedElement {

    private String id;





    private requirement_Repository requirement_repository;




    private requirement_Category requirement_category;




    private List<requirement_Requirement> requirement_requirements;




    private requirement_Repository requirement_repository;




    private requirement_Category requirement_category;




    private requirement_Requirement requirement_requirement;


    public requirement_Category(
        String id    ) {
        super(
        );
        this.id = id;
        this.requirement_requirements = new ArrayList<>();
    }

    public requirement_Category(
        String id        ArrayList<requirement_Requirement> requirement_requirements    ) {
        this.id = id;
        this.requirement_requirements = requirement_requirements;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public requirement_Repository getRequirement_repository() {
        return requirement_repository;
    }

    public void setRequirement_repository(requirement_Repository requirement_repository) {
        this.requirement_repository = requirement_repository;
    }
    public requirement_Category getRequirement_category() {
        return requirement_category;
    }

    public void setRequirement_category(requirement_Category requirement_category) {
        this.requirement_category = requirement_category;
    }
    public List<requirement_Requirement> getRequirement_requirements() {
        return requirement_requirements;
    }

    public void addRequirement_requirement(Requirement_requirement requirement_requirement) {
        this.requirement_requirements.add(requirement_requirement);
    }
    public requirement_Repository getRequirement_repository() {
        return requirement_repository;
    }

    public void setRequirement_repository(requirement_Repository requirement_repository) {
        this.requirement_repository = requirement_repository;
    }
    public requirement_Category getRequirement_category() {
        return requirement_category;
    }

    public void setRequirement_category(requirement_Category requirement_category) {
        this.requirement_category = requirement_category;
    }
    public requirement_Requirement getRequirement_requirement() {
        return requirement_requirement;
    }

    public void setRequirement_requirement(requirement_Requirement requirement_requirement) {
        this.requirement_requirement = requirement_requirement;
    }

}