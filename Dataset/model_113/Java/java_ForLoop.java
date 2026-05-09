





import java.util.List;
import java.util.ArrayList;

public class java_ForLoop extends Conditional, Statement, StatementContainer {






    private List<java_Expression> java_expressions;




    private java_ForLoopInitializer java_forloopinitializer;


    public java_ForLoop(
    ) {
        super(
        );
        this.java_expressions = new ArrayList<>();
    }

    public java_ForLoop(
        ArrayList<java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
    }


    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }
    public java_ForLoopInitializer getJava_forloopinitializer() {
        return java_forloopinitializer;
    }

    public void setJava_forloopinitializer(java_ForLoopInitializer java_forloopinitializer) {
        this.java_forloopinitializer = java_forloopinitializer;
    }

}