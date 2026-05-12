





import java.util.List;
import java.util.ArrayList;

public class requirements_editor_Category  {

    private String name;





    private List<requirements_editor_Category> requirements_editor_categorys;




    private requirements_editor_Person requirements_editor_person;




    private requirements_editor_Person requirements_editor_person;




    private List<requirements_editor_Requirement> requirements_editor_requirements;


    public requirements_editor_Category(
        String name    ) {
        this.name = name;
        this.requirements_editor_categorys = new ArrayList<>();
        this.requirements_editor_requirements = new ArrayList<>();
    }

    public requirements_editor_Category(
        String name        ArrayList<requirements_editor_Category> requirements_editor_categorys,        ArrayList<requirements_editor_Requirement> requirements_editor_requirements    ) {
        this.name = name;
        this.requirements_editor_categorys = requirements_editor_categorys;
        this.requirements_editor_requirements = requirements_editor_requirements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<requirements_editor_Category> getRequirements_editor_categorys() {
        return requirements_editor_categorys;
    }

    public void addRequirements_editor_category(Requirements_editor_category requirements_editor_category) {
        this.requirements_editor_categorys.add(requirements_editor_category);
    }
    public requirements_editor_Person getRequirements_editor_person() {
        return requirements_editor_person;
    }

    public void setRequirements_editor_person(requirements_editor_Person requirements_editor_person) {
        this.requirements_editor_person = requirements_editor_person;
    }
    public requirements_editor_Person getRequirements_editor_person() {
        return requirements_editor_person;
    }

    public void setRequirements_editor_person(requirements_editor_Person requirements_editor_person) {
        this.requirements_editor_person = requirements_editor_person;
    }
    public List<requirements_editor_Requirement> getRequirements_editor_requirements() {
        return requirements_editor_requirements;
    }

    public void addRequirements_editor_requirement(Requirements_editor_requirement requirements_editor_requirement) {
        this.requirements_editor_requirements.add(requirements_editor_requirement);
    }

}