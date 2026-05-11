





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_RequirementGroup extends Requirement {

    private String requirementOperator;



    public camel_requirement_RequirementGroup(
        String requirementOperator    ) {
        super(
        );
        this.requirementOperator = requirementOperator;
    }


    public String getRequirementoperator() {
        return requirementOperator;
    }

    public void setRequirementoperator(String requirementOperator) {
        this.requirementOperator = requirementOperator;
    }


}