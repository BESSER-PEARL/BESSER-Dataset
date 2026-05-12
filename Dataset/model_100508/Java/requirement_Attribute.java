





import java.util.List;
import java.util.ArrayList;

public class requirement_Attribute extends EModelElement {

    private String name;





    private requirement_Requirement requirement_requirement;


    public requirement_Attribute(
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

    public requirement_Requirement getRequirement_requirement() {
        return requirement_requirement;
    }

    public void setRequirement_requirement(requirement_Requirement requirement_requirement) {
        this.requirement_requirement = requirement_requirement;
    }

}