





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ForStatement extends Statement {






    private List<JDTAST_Expression> jdtast_expressions;




    private JDTAST_Expression jdtast_expression;




    private List<JDTAST_Expression> jdtast_expressions;




    private JDTAST_Statement jdtast_statement;


    public JDTAST_ForStatement(
    ) {
        super(
        );
        this.jdtast_expressions = new ArrayList<>();
        this.jdtast_expressions = new ArrayList<>();
    }

    public JDTAST_ForStatement(
        ArrayList<JDTAST_Expression> jdtast_expressions,        ArrayList<JDTAST_Expression> jdtast_expressions    ) {
        this.jdtast_expressions = jdtast_expressions;
        this.jdtast_expressions = jdtast_expressions;
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
    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }
    public JDTAST_Statement getJdtast_statement() {
        return jdtast_statement;
    }

    public void setJdtast_statement(JDTAST_Statement jdtast_statement) {
        this.jdtast_statement = jdtast_statement;
    }

}