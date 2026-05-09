





import java.util.List;
import java.util.ArrayList;

public class JDTAST_SwitchStatement extends Statement {






    private JDTAST_Expression jdtast_expression;




    private List<JDTAST_Statement> jdtast_statements;


    public JDTAST_SwitchStatement(
    ) {
        super(
        );
        this.jdtast_statements = new ArrayList<>();
    }

    public JDTAST_SwitchStatement(
        ArrayList<JDTAST_Statement> jdtast_statements    ) {
        this.jdtast_statements = jdtast_statements;
    }


    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }
    public List<JDTAST_Statement> getJdtast_statements() {
        return jdtast_statements;
    }

    public void addJdtast_statement(Jdtast_statement jdtast_statement) {
        this.jdtast_statements.add(jdtast_statement);
    }

}