





import java.util.List;
import java.util.ArrayList;

public class newP_SimpleDependency extends Dependency {

    private String name;





    private newP_RequirementTerm newp_requirementterm;


    public newP_SimpleDependency(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public newP_RequirementTerm getNewp_requirementterm() {
        return newp_requirementterm;
    }

    public void setNewp_requirementterm(newP_RequirementTerm newp_requirementterm) {
        this.newp_requirementterm = newp_requirementterm;
    }

}