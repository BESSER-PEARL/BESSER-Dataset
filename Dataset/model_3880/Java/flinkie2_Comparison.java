





import java.util.List;
import java.util.ArrayList;

public class flinkie2_Comparison extends BoolExpr {

    private String operator;



    public flinkie2_Comparison(
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