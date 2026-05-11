





import java.util.List;
import java.util.ArrayList;

public class adwithoutruntime_IntegerComparisonExpression extends IntegerExpression {

    private String operator;





    private adwithoutruntime_BooleanVariable adwithoutruntime_booleanvariable;


    public adwithoutruntime_IntegerComparisonExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public adwithoutruntime_BooleanVariable getAdwithoutruntime_booleanvariable() {
        return adwithoutruntime_booleanvariable;
    }

    public void setAdwithoutruntime_booleanvariable(adwithoutruntime_BooleanVariable adwithoutruntime_booleanvariable) {
        this.adwithoutruntime_booleanvariable = adwithoutruntime_booleanvariable;
    }

}