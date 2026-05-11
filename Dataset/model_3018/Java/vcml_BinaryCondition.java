





import java.util.List;
import java.util.ArrayList;

public class vcml_BinaryCondition extends Condition {

    private String operator;





    private vcml_Condition vcml_condition;




    private vcml_Condition vcml_condition;


    public vcml_BinaryCondition(
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

    public vcml_Condition getVcml_condition() {
        return vcml_condition;
    }

    public void setVcml_condition(vcml_Condition vcml_condition) {
        this.vcml_condition = vcml_condition;
    }
    public vcml_Condition getVcml_condition() {
        return vcml_condition;
    }

    public void setVcml_condition(vcml_Condition vcml_condition) {
        this.vcml_condition = vcml_condition;
    }

}