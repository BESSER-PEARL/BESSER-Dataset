





import java.util.List;
import java.util.ArrayList;

public class iot2_IntegerCalculationExpression extends IntegerExpression {

    private String operator;





    private iot2_IntegerVariable iot2_integervariable;


    public iot2_IntegerCalculationExpression(
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

    public iot2_IntegerVariable getIot2_integervariable() {
        return iot2_integervariable;
    }

    public void setIot2_integervariable(iot2_IntegerVariable iot2_integervariable) {
        this.iot2_integervariable = iot2_integervariable;
    }

}