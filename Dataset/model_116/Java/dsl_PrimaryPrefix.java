





import java.util.List;
import java.util.ArrayList;

public class dsl_PrimaryPrefix  {

    private String superOp;
    private String thisOp;
    private String id;





    private dsl_ResultType dsl_resulttype;




    private dsl_Expression dsl_expression;




    private dsl_Literal dsl_literal;


    public dsl_PrimaryPrefix(
        String superOp,        String thisOp,        String id    ) {
        this.superOp = superOp;
        this.thisOp = thisOp;
        this.id = id;
    }


    public String getSuperop() {
        return superOp;
    }

    public void setSuperop(String superOp) {
        this.superOp = superOp;
    }
    public String getThisop() {
        return thisOp;
    }

    public void setThisop(String thisOp) {
        this.thisOp = thisOp;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_ResultType getDsl_resulttype() {
        return dsl_resulttype;
    }

    public void setDsl_resulttype(dsl_ResultType dsl_resulttype) {
        this.dsl_resulttype = dsl_resulttype;
    }
    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }
    public dsl_Literal getDsl_literal() {
        return dsl_literal;
    }

    public void setDsl_literal(dsl_Literal dsl_literal) {
        this.dsl_literal = dsl_literal;
    }

}