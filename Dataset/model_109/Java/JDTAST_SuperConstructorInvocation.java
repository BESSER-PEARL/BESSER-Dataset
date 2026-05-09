





import java.util.List;
import java.util.ArrayList;

public class JDTAST_SuperConstructorInvocation extends Statement {






    private List<JDTAST_Expression> jdtast_expressions;




    private List<JDTAST_Type> jdtast_types;




    private JDTAST_Expression jdtast_expression;


    public JDTAST_SuperConstructorInvocation(
    ) {
        super(
        );
        this.jdtast_expressions = new ArrayList<>();
        this.jdtast_types = new ArrayList<>();
    }

    public JDTAST_SuperConstructorInvocation(
        ArrayList<JDTAST_Expression> jdtast_expressions,        ArrayList<JDTAST_Type> jdtast_types    ) {
        this.jdtast_expressions = jdtast_expressions;
        this.jdtast_types = jdtast_types;
    }


    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }
    public List<JDTAST_Type> getJdtast_types() {
        return jdtast_types;
    }

    public void addJdtast_type(Jdtast_type jdtast_type) {
        this.jdtast_types.add(jdtast_type);
    }
    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }

}