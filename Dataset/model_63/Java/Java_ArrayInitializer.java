





import java.util.List;
import java.util.ArrayList;

public class Java_ArrayInitializer extends Expression {






    private List<Java_Expression> java_expressions;




    private Java_ArrayCreation java_arraycreation;


    public Java_ArrayInitializer(
    ) {
        super(
        );
        this.java_expressions = new ArrayList<>();
    }

    public Java_ArrayInitializer(
        ArrayList<Java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
    }


    public List<Java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }
    public Java_ArrayCreation getJava_arraycreation() {
        return java_arraycreation;
    }

    public void setJava_arraycreation(Java_ArrayCreation java_arraycreation) {
        this.java_arraycreation = java_arraycreation;
    }

}