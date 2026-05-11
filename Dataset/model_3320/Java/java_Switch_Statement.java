





import java.util.List;
import java.util.ArrayList;

public class java_Switch_Statement  {






    private java_Expression java_expression;




    private List<java_Expression> java_expressions;




    private List<java_Statement> java_statements;




    private java_Statement java_statement;


    public java_Switch_Statement(
    ) {
        this.java_expressions = new ArrayList<>();
        this.java_statements = new ArrayList<>();
    }

    public java_Switch_Statement(
        ArrayList<java_Expression> java_expressions,        ArrayList<java_Statement> java_statements    ) {
        this.java_expressions = java_expressions;
        this.java_statements = java_statements;
    }


    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }
    public List<java_Statement> getJava_statements() {
        return java_statements;
    }

    public void addJava_statement(Java_statement java_statement) {
        this.java_statements.add(java_statement);
    }
    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }

}