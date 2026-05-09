





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_CompositeConditionExpression extends ConditionExpression {






    private List<appBuilderDSL_Condition> appbuilderdsl_conditions;


    public appBuilderDSL_CompositeConditionExpression(
    ) {
        super(
        );
        this.appbuilderdsl_conditions = new ArrayList<>();
    }

    public appBuilderDSL_CompositeConditionExpression(
        ArrayList<appBuilderDSL_Condition> appbuilderdsl_conditions    ) {
        this.appbuilderdsl_conditions = appbuilderdsl_conditions;
    }


    public List<appBuilderDSL_Condition> getAppbuilderdsl_conditions() {
        return appbuilderdsl_conditions;
    }

    public void addAppbuilderdsl_condition(Appbuilderdsl_condition appbuilderdsl_condition) {
        this.appbuilderdsl_conditions.add(appbuilderdsl_condition);
    }

}