





import java.util.List;
import java.util.ArrayList;

public class JDTAST_MethodInvocation extends Expression {






    private JDTAST_IMethod jdtast_imethod;




    private List<JDTAST_Type> jdtast_types;




    private JDTAST_SimpleName jdtast_simplename;




    private List<JDTAST_Expression> jdtast_expressions;




    private JDTAST_Expression jdtast_expression;


    public JDTAST_MethodInvocation(
    ) {
        super(
        );
        this.jdtast_types = new ArrayList<>();
        this.jdtast_expressions = new ArrayList<>();
    }

    public JDTAST_MethodInvocation(
        ArrayList<JDTAST_Type> jdtast_types,        ArrayList<JDTAST_Expression> jdtast_expressions    ) {
        this.jdtast_types = jdtast_types;
        this.jdtast_expressions = jdtast_expressions;
    }


    public JDTAST_IMethod getJdtast_imethod() {
        return jdtast_imethod;
    }

    public void setJdtast_imethod(JDTAST_IMethod jdtast_imethod) {
        this.jdtast_imethod = jdtast_imethod;
    }
    public List<JDTAST_Type> getJdtast_types() {
        return jdtast_types;
    }

    public void addJdtast_type(Jdtast_type jdtast_type) {
        this.jdtast_types.add(jdtast_type);
    }
    public JDTAST_SimpleName getJdtast_simplename() {
        return jdtast_simplename;
    }

    public void setJdtast_simplename(JDTAST_SimpleName jdtast_simplename) {
        this.jdtast_simplename = jdtast_simplename;
    }
    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }
    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }

}