





import java.util.List;
import java.util.ArrayList;

public class java_AbstractMethodInvocation extends ASTNode {






    private List<java_Expression> java_expressions;


    public java_AbstractMethodInvocation(
    ) {
        super(
        );
        this.java_expressions = new ArrayList<>();
    }

    public java_AbstractMethodInvocation(
        ArrayList<java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
    }


    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }

}