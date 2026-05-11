





import java.util.List;
import java.util.ArrayList;

public class adwithoutruntime_IntegerCalculationExpression extends IntegerExpression {

    private String operator;





    private adwithoutruntime_IntegerVariable adwithoutruntime_integervariable;


    public adwithoutruntime_IntegerCalculationExpression(
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

    public adwithoutruntime_IntegerVariable getAdwithoutruntime_integervariable() {
        return adwithoutruntime_integervariable;
    }

    public void setAdwithoutruntime_integervariable(adwithoutruntime_IntegerVariable adwithoutruntime_integervariable) {
        this.adwithoutruntime_integervariable = adwithoutruntime_integervariable;
    }

}