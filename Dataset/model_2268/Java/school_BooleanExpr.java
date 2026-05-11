





import java.util.List;
import java.util.ArrayList;

public class school_BooleanExpr  {

    private String rhs;
    private String operator;
    private String lhs;





    private school_Where school_where;




    private school_BooleanExpr school_booleanexpr;




    private school_BooleanExpr school_booleanexpr;


    public school_BooleanExpr(
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

    public school_Where getSchool_where() {
        return school_where;
    }

    public void setSchool_where(school_Where school_where) {
        this.school_where = school_where;
    }
    public school_BooleanExpr getSchool_booleanexpr() {
        return school_booleanexpr;
    }

    public void setSchool_booleanexpr(school_BooleanExpr school_booleanexpr) {
        this.school_booleanexpr = school_booleanexpr;
    }
    public school_BooleanExpr getSchool_booleanexpr() {
        return school_booleanexpr;
    }

    public void setSchool_booleanexpr(school_BooleanExpr school_booleanexpr) {
        this.school_booleanexpr = school_booleanexpr;
    }

}