





import java.util.List;
import java.util.ArrayList;

public class flinkie2_TwoOpInt extends IntExpr {

    private String operator;



    public flinkie2_TwoOpInt(
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