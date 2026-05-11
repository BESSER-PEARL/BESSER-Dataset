





import java.util.List;
import java.util.ArrayList;

public class dsl_Expression  {

    private String lhs;
    private String operator;
    private String rhs;



    public dsl_Expression(
        String lhs,        String operator,        String rhs    ) {
        this.lhs = lhs;
        this.operator = operator;
        this.rhs = rhs;
    }


    public String getLhs() {
        return lhs;
    }

    public void setLhs(String lhs) {
        this.lhs = lhs;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getRhs() {
        return rhs;
    }

    public void setRhs(String rhs) {
        this.rhs = rhs;
    }


}