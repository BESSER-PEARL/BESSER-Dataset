





import java.util.List;
import java.util.ArrayList;

public class rover_TriggeredTransition extends Transition {

    private String Operator;



    public rover_TriggeredTransition(
        String Operator    ) {
        super(
        );
        this.Operator = Operator;
    }


    public String getOperator() {
        return Operator;
    }

    public void setOperator(String Operator) {
        this.Operator = Operator;
    }


}