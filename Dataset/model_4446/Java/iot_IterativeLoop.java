





import java.util.List;
import java.util.ArrayList;

public class iot_IterativeLoop extends Iteration {

    private String operator;
    private String var;





    private iot_ConditionPort iot_conditionport;


    public iot_IterativeLoop(
        String operator,        String var    ) {
        super(
        );
        this.operator = operator;
        this.var = var;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }

    public iot_ConditionPort getIot_conditionport() {
        return iot_conditionport;
    }

    public void setIot_conditionport(iot_ConditionPort iot_conditionport) {
        this.iot_conditionport = iot_conditionport;
    }

}