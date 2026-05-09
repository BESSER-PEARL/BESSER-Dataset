





import java.util.List;
import java.util.ArrayList;

public class java_SwitchStatement extends Statement {






    private java_Expression java_expression;




    private List<java_Statement> java_statements;


    public java_SwitchStatement(
    ) {
        super(
        );
        this.java_statements = new ArrayList<>();
    }

    public java_SwitchStatement(
        ArrayList<java_Statement> java_statements    ) {
        this.java_statements = java_statements;
    }


    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public List<java_Statement> getJava_statements() {
        return java_statements;
    }

    public void addJava_statement(Java_statement java_statement) {
        this.java_statements.add(java_statement);
    }

}