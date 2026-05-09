





import java.util.List;
import java.util.ArrayList;

public class javaMM_SwitchStatement extends Statement {






    private List<javaMM_Statement> javamm_statements;




    private javaMM_Expression javamm_expression;


    public javaMM_SwitchStatement(
    ) {
        super(
        );
        this.javamm_statements = new ArrayList<>();
    }

    public javaMM_SwitchStatement(
        ArrayList<javaMM_Statement> javamm_statements    ) {
        this.javamm_statements = javamm_statements;
    }


    public List<javaMM_Statement> getJavamm_statements() {
        return javamm_statements;
    }

    public void addJavamm_statement(Javamm_statement javamm_statement) {
        this.javamm_statements.add(javamm_statement);
    }
    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }

}