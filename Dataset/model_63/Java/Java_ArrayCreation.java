





import java.util.List;
import java.util.ArrayList;

public class Java_ArrayCreation extends Expression {






    private List<Java_Expression> java_expressions;


    public Java_ArrayCreation(
    ) {
        super(
        );
        this.java_expressions = new ArrayList<>();
    }

    public Java_ArrayCreation(
        ArrayList<Java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
    }


    public List<Java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }

}