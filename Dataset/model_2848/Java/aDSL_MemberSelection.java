





import java.util.List;
import java.util.ArrayList;

public class aDSL_MemberSelection extends Expression {

    private boolean methodinvocation;
    private boolean ispar;





    private List<aDSL_Expression> adsl_expressions;




    private aDSL_Expression adsl_expression;




    private aDSL_Member adsl_member;




    private aDSL_XClass adsl_xclass;


    public aDSL_MemberSelection(
        boolean methodinvocation,        boolean ispar    ) {
        super(
        );
        this.methodinvocation = methodinvocation;
        this.ispar = ispar;
        this.adsl_expressions = new ArrayList<>();
    }

    public aDSL_MemberSelection(
        boolean methodinvocation,        boolean ispar        ArrayList<aDSL_Expression> adsl_expressions    ) {
        this.methodinvocation = methodinvocation;
        this.ispar = ispar;
        this.adsl_expressions = adsl_expressions;
    }

    public boolean getMethodinvocation() {
        return methodinvocation;
    }

    public void setMethodinvocation(boolean methodinvocation) {
        this.methodinvocation = methodinvocation;
    }
    public boolean getIspar() {
        return ispar;
    }

    public void setIspar(boolean ispar) {
        this.ispar = ispar;
    }

    public List<aDSL_Expression> getAdsl_expressions() {
        return adsl_expressions;
    }

    public void addAdsl_expression(Adsl_expression adsl_expression) {
        this.adsl_expressions.add(adsl_expression);
    }
    public aDSL_Expression getAdsl_expression() {
        return adsl_expression;
    }

    public void setAdsl_expression(aDSL_Expression adsl_expression) {
        this.adsl_expression = adsl_expression;
    }
    public aDSL_Member getAdsl_member() {
        return adsl_member;
    }

    public void setAdsl_member(aDSL_Member adsl_member) {
        this.adsl_member = adsl_member;
    }
    public aDSL_XClass getAdsl_xclass() {
        return adsl_xclass;
    }

    public void setAdsl_xclass(aDSL_XClass adsl_xclass) {
        this.adsl_xclass = adsl_xclass;
    }

}