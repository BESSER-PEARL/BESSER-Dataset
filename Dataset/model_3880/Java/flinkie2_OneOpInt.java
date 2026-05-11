





import java.util.List;
import java.util.ArrayList;

public class flinkie2_OneOpInt extends IntExpr {

    private String operator;





    private flinkie2_IntExpr flinkie2_intexpr;


    public flinkie2_OneOpInt(
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

    public flinkie2_IntExpr getFlinkie2_intexpr() {
        return flinkie2_intexpr;
    }

    public void setFlinkie2_intexpr(flinkie2_IntExpr flinkie2_intexpr) {
        this.flinkie2_intexpr = flinkie2_intexpr;
    }

}