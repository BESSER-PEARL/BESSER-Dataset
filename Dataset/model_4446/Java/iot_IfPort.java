





import java.util.List;
import java.util.ArrayList;

public class iot_IfPort extends RequiredPort {

    private String operator;
    private boolean condition;
    private String var;



    public iot_IfPort(
        String operator,        boolean condition,        String var    ) {
        super(
        );
        this.operator = operator;
        this.condition = condition;
        this.var = var;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public boolean getCondition() {
        return condition;
    }

    public void setCondition(boolean condition) {
        this.condition = condition;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }


}