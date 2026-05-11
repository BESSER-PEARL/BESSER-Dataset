





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Condition extends NamedElement {

    private String operator;



    public arduinoML_Condition(
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


}