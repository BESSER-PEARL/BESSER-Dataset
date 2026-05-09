





import java.util.List;
import java.util.ArrayList;

public class ccsl_action_ArithmeticOperatorMap  {

    private String newArithmeticOperator;
    private String oldArithmeticOperator;



    public ccsl_action_ArithmeticOperatorMap(
        String newArithmeticOperator,        String oldArithmeticOperator    ) {
        this.newArithmeticOperator = newArithmeticOperator;
        this.oldArithmeticOperator = oldArithmeticOperator;
    }


    public String getNewarithmeticoperator() {
        return newArithmeticOperator;
    }

    public void setNewarithmeticoperator(String newArithmeticOperator) {
        this.newArithmeticOperator = newArithmeticOperator;
    }
    public String getOldarithmeticoperator() {
        return oldArithmeticOperator;
    }

    public void setOldarithmeticoperator(String oldArithmeticOperator) {
        this.oldArithmeticOperator = oldArithmeticOperator;
    }


}