





import java.util.List;
import java.util.ArrayList;

public class newP_Person  {

    private String firstName;
    private String lastName;





    private List<newP_Requirement> newp_requirements;




    private newP_Specification newp_specification;




    private List<newP_Category> newp_categorys;


    public newP_Person(
        String firstName,        String lastName    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.newp_requirements = new ArrayList<>();
        this.newp_categorys = new ArrayList<>();
    }

    public newP_Person(
        String firstName,        String lastName        ArrayList<newP_Requirement> newp_requirements,        ArrayList<newP_Category> newp_categorys    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.newp_requirements = newp_requirements;
        this.newp_categorys = newp_categorys;
    }

    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public List<newP_Requirement> getNewp_requirements() {
        return newp_requirements;
    }

    public void addNewp_requirement(Newp_requirement newp_requirement) {
        this.newp_requirements.add(newp_requirement);
    }
    public newP_Specification getNewp_specification() {
        return newp_specification;
    }

    public void setNewp_specification(newP_Specification newp_specification) {
        this.newp_specification = newp_specification;
    }
    public List<newP_Category> getNewp_categorys() {
        return newp_categorys;
    }

    public void addNewp_category(Newp_category newp_category) {
        this.newp_categorys.add(newp_category);
    }

}