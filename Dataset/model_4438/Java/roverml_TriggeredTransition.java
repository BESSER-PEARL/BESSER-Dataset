





import java.util.List;
import java.util.ArrayList;

public class roverml_TriggeredTransition extends Transition {

    private String operator;



    public roverml_TriggeredTransition(
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