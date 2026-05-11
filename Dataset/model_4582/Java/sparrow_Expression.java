





import java.util.List;
import java.util.ArrayList;

public class sparrow_Expression  {

    private String rhs;
    private String operator;
    private String lhs;



    public sparrow_Expression(
        String rhs,        String operator,        String lhs    ) {
        this.rhs = rhs;
        this.operator = operator;
        this.lhs = lhs;
    }


    public String getRhs() {
        return rhs;
    }

    public void setRhs(String rhs) {
        this.rhs = rhs;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getLhs() {
        return lhs;
    }

    public void setLhs(String lhs) {
        this.lhs = lhs;
    }


}