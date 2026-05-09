





import java.util.List;
import java.util.ArrayList;

public class javaMM_ForStatement extends Statement {






    private javaMM_Expression javamm_expression;




    private List<javaMM_Expression> javamm_expressions;




    private javaMM_Statement javamm_statement;




    private List<javaMM_Expression> javamm_expressions;


    public javaMM_ForStatement(
    ) {
        super(
        );
        this.javamm_expressions = new ArrayList<>();
        this.javamm_expressions = new ArrayList<>();
    }

    public javaMM_ForStatement(
        ArrayList<javaMM_Expression> javamm_expressions,        ArrayList<javaMM_Expression> javamm_expressions    ) {
        this.javamm_expressions = javamm_expressions;
        this.javamm_expressions = javamm_expressions;
    }


    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }
    public List<javaMM_Expression> getJavamm_expressions() {
        return javamm_expressions;
    }

    public void addJavamm_expression(Javamm_expression javamm_expression) {
        this.javamm_expressions.add(javamm_expression);
    }
    public javaMM_Statement getJavamm_statement() {
        return javamm_statement;
    }

    public void setJavamm_statement(javaMM_Statement javamm_statement) {
        this.javamm_statement = javamm_statement;
    }
    public List<javaMM_Expression> getJavamm_expressions() {
        return javamm_expressions;
    }

    public void addJavamm_expression(Javamm_expression javamm_expression) {
        this.javamm_expressions.add(javamm_expression);
    }

}