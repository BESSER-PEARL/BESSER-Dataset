





import java.util.List;
import java.util.ArrayList;

public class Java_SwitchStatement extends Statement {






    private List<Java_Statement> java_statements;




    private Java_Expression java_expression;


    public Java_SwitchStatement(
    ) {
        super(
        );
        this.java_statements = new ArrayList<>();
    }

    public Java_SwitchStatement(
        ArrayList<Java_Statement> java_statements    ) {
        this.java_statements = java_statements;
    }


    public List<Java_Statement> getJava_statements() {
        return java_statements;
    }

    public void addJava_statement(Java_statement java_statement) {
        this.java_statements.add(java_statement);
    }
    public Java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(Java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}