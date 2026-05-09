





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_TaskSymmetryRestriction extends restrictions_TaskGroupRestrictionA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, scenario_ModeDependentElementA, restrictions_TaskRestrictionA, scenario_VariantDependentElementA {

    private String type;



    public oaam_restrictions_TaskSymmetryRestriction(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}