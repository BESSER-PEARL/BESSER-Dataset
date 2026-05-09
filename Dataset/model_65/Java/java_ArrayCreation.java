





import java.util.List;
import java.util.ArrayList;

public class java_ArrayCreation extends Expression {






    private java_ArrayInitializer java_arrayinitializer;




    private java_TypeAccess java_typeaccess;




    private List<java_Expression> java_expressions;


    public java_ArrayCreation(
    ) {
        super(
        );
        this.java_expressions = new ArrayList<>();
    }

    public java_ArrayCreation(
        ArrayList<java_Expression> java_expressions    ) {
        this.java_expressions = java_expressions;
    }


    public java_ArrayInitializer getJava_arrayinitializer() {
        return java_arrayinitializer;
    }

    public void setJava_arrayinitializer(java_ArrayInitializer java_arrayinitializer) {
        this.java_arrayinitializer = java_arrayinitializer;
    }
    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }

}