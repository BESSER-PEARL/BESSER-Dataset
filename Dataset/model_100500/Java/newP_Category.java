





import java.util.List;
import java.util.ArrayList;

public class newP_Category  {

    private String name;





    private newP_Category newp_category;




    private List<newP_Requirement> newp_requirements;


    public newP_Category(
        String name    ) {
        this.name = name;
        this.newp_requirements = new ArrayList<>();
    }

    public newP_Category(
        String name        ArrayList<newP_Requirement> newp_requirements    ) {
        this.name = name;
        this.newp_requirements = newp_requirements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public newP_Category getNewp_category() {
        return newp_category;
    }

    public void setNewp_category(newP_Category newp_category) {
        this.newp_category = newp_category;
    }
    public List<newP_Requirement> getNewp_requirements() {
        return newp_requirements;
    }

    public void addNewp_requirement(Newp_requirement newp_requirement) {
        this.newp_requirements.add(newp_requirement);
    }

}