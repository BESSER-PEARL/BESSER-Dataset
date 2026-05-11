





import java.util.List;
import java.util.ArrayList;

public class java_Arg_List  {






    private java_Expression_aux java_expression_aux;




    private List<java_Expression> java_expressions;




    private java_Creating_Expression java_creating_expression;




    private java_Expression java_expression;


    public java_Arg_List(
    ) {
        this.java_expressions = new ArrayList<>();
    }

    public java_Arg_List(
        ArrayList<java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
    }


    public java_Expression_aux getJava_expression_aux() {
        return java_expression_aux;
    }

    public void setJava_expression_aux(java_Expression_aux java_expression_aux) {
        this.java_expression_aux = java_expression_aux;
    }
    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }
    public java_Creating_Expression getJava_creating_expression() {
        return java_creating_expression;
    }

    public void setJava_creating_expression(java_Creating_Expression java_creating_expression) {
        this.java_creating_expression = java_creating_expression;
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}