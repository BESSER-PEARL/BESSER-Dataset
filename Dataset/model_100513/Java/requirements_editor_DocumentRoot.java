





import java.util.List;
import java.util.ArrayList;

public class requirements_editor_DocumentRoot  {

    private String name;





    private List<requirements_editor_Person> requirements_editor_persons;




    private List<requirements_editor_Category> requirements_editor_categorys;


    public requirements_editor_DocumentRoot(
        String name    ) {
        this.name = name;
        this.requirements_editor_persons = new ArrayList<>();
        this.requirements_editor_categorys = new ArrayList<>();
    }

    public requirements_editor_DocumentRoot(
        String name        ArrayList<requirements_editor_Person> requirements_editor_persons,        ArrayList<requirements_editor_Category> requirements_editor_categorys    ) {
        this.name = name;
        this.requirements_editor_persons = requirements_editor_persons;
        this.requirements_editor_categorys = requirements_editor_categorys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<requirements_editor_Person> getRequirements_editor_persons() {
        return requirements_editor_persons;
    }

    public void addRequirements_editor_person(Requirements_editor_person requirements_editor_person) {
        this.requirements_editor_persons.add(requirements_editor_person);
    }
    public List<requirements_editor_Category> getRequirements_editor_categorys() {
        return requirements_editor_categorys;
    }

    public void addRequirements_editor_category(Requirements_editor_category requirements_editor_category) {
        this.requirements_editor_categorys.add(requirements_editor_category);
    }

}