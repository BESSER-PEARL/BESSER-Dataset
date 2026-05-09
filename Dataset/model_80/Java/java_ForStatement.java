





import java.util.List;
import java.util.ArrayList;

public class java_ForStatement extends Statement {






    private List<java_Expression> java_expressions;




    private java_Expression java_expression;




    private List<java_Expression> java_expressions;




    private java_Statement java_statement;


    public java_ForStatement(
    ) {
        super(
        );
        this.java_expressions = new ArrayList<>();
        this.java_expressions = new ArrayList<>();
    }

    public java_ForStatement(
        ArrayList<java_Expression> java_expressions,        ArrayList<java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
        this.java_expressions = java_expressions;
    }


    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
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
    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }

}