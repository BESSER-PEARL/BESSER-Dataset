





import java.util.List;
import java.util.ArrayList;

public class simple_lang_IfStatement extends Statement {






    private List<simple_lang_Statement> simple_lang_statements;




    private simple_lang_Expression simple_lang_expression;




    private List<simple_lang_Statement> simple_lang_statements;


    public simple_lang_IfStatement(
    ) {
        super(
        );
        this.simple_lang_statements = new ArrayList<>();
        this.simple_lang_statements = new ArrayList<>();
    }

    public simple_lang_IfStatement(
        ArrayList<simple_lang_Statement> simple_lang_statements,        ArrayList<simple_lang_Statement> simple_lang_statements    ) {
        this.simple_lang_statements = simple_lang_statements;
        this.simple_lang_statements = simple_lang_statements;
    }


    public List<simple_lang_Statement> getSimple_lang_statements() {
        return simple_lang_statements;
    }

    public void addSimple_lang_statement(Simple_lang_statement simple_lang_statement) {
        this.simple_lang_statements.add(simple_lang_statement);
    }
    public simple_lang_Expression getSimple_lang_expression() {
        return simple_lang_expression;
    }

    public void setSimple_lang_expression(simple_lang_Expression simple_lang_expression) {
        this.simple_lang_expression = simple_lang_expression;
    }
    public List<simple_lang_Statement> getSimple_lang_statements() {
        return simple_lang_statements;
    }

    public void addSimple_lang_statement(Simple_lang_statement simple_lang_statement) {
        this.simple_lang_statements.add(simple_lang_statement);
    }

}