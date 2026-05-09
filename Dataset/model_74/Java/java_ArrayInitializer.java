





import java.util.List;
import java.util.ArrayList;

public class java_ArrayInitializer extends Expression {






    private List<java_Expression> java_expressions;




    private java_ArrayCreation java_arraycreation;


    public java_ArrayInitializer(
    ) {
        super(
        );
        this.java_expressions = new ArrayList<>();
    }

    public java_ArrayInitializer(
        ArrayList<java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
    }


    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }
    public java_ArrayCreation getJava_arraycreation() {
        return java_arraycreation;
    }

    public void setJava_arraycreation(java_ArrayCreation java_arraycreation) {
        this.java_arraycreation = java_arraycreation;
    }

}