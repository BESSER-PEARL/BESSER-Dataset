





import java.util.List;
import java.util.ArrayList;

public class FPath_OperatorExp extends Expression {

    private String operator;



    public FPath_OperatorExp(
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