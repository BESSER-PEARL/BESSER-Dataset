





import java.util.List;
import java.util.ArrayList;

public class arduinoml_MultipleCondition extends Condition {

    private String operators;



    public arduinoml_MultipleCondition(
        String operators    ) {
        super(
        );
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }


}