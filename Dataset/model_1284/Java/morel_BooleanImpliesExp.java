





import java.util.List;
import java.util.ArrayList;

public class morel_BooleanImpliesExp extends Expression {

    private String operator;





    private morel_ConditionExp morel_conditionexp;


    public morel_BooleanImpliesExp(
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

    public morel_ConditionExp getMorel_conditionexp() {
        return morel_conditionexp;
    }

    public void setMorel_conditionexp(morel_ConditionExp morel_conditionexp) {
        this.morel_conditionexp = morel_conditionexp;
    }

}