





import java.util.List;
import java.util.ArrayList;

public class java_Variable_initializer  {






    private List<java_Variable_initializer> java_variable_initializers;




    private java_Variable_declarator java_variable_declarator;




    private java_Variable_initializer java_variable_initializer;


    public java_Variable_initializer(
    ) {
        this.java_variable_initializers = new ArrayList<>();
    }

    public java_Variable_initializer(
        ArrayList<java_Variable_initializer> java_variable_initializers    ) {
        this.java_variable_initializers = java_variable_initializers;
    }


    public List<java_Variable_initializer> getJava_variable_initializers() {
        return java_variable_initializers;
    }

    public void addJava_variable_initializer(Java_variable_initializer java_variable_initializer) {
        this.java_variable_initializers.add(java_variable_initializer);
    }
    public java_Variable_declarator getJava_variable_declarator() {
        return java_variable_declarator;
    }

    public void setJava_variable_declarator(java_Variable_declarator java_variable_declarator) {
        this.java_variable_declarator = java_variable_declarator;
    }
    public java_Variable_initializer getJava_variable_initializer() {
        return java_variable_initializer;
    }

    public void setJava_variable_initializer(java_Variable_initializer java_variable_initializer) {
        this.java_variable_initializer = java_variable_initializer;
    }

}