





import java.util.List;
import java.util.ArrayList;

public class flinkie2_OneOpBool extends BoolExpr {

    private String operator;





    private flinkie2_BoolExpr flinkie2_boolexpr;


    public flinkie2_OneOpBool(
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

    public flinkie2_BoolExpr getFlinkie2_boolexpr() {
        return flinkie2_boolexpr;
    }

    public void setFlinkie2_boolexpr(flinkie2_BoolExpr flinkie2_boolexpr) {
        this.flinkie2_boolexpr = flinkie2_boolexpr;
    }

}