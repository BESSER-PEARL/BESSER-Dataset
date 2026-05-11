





import java.util.List;
import java.util.ArrayList;

public class java_Expression  {

    private String super;
    private String null;
    private String name;
    private String this;





    private java_Literal_Expression java_literal_expression;




    private java_Variable_initializer java_variable_initializer;


    public java_Expression(
        String super,        String null,        String name,        String this    ) {
        this.super = super;
        this.null = null;
        this.name = name;
        this.this = this;
    }


    public String getSuper() {
        return super;
    }

    public void setSuper(String super) {
        this.super = super;
    }
    public String getNull() {
        return null;
    }

    public void setNull(String null) {
        this.null = null;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getThis() {
        return this;
    }

    public void setThis(String this) {
        this.this = this;
    }

    public java_Literal_Expression getJava_literal_expression() {
        return java_literal_expression;
    }

    public void setJava_literal_expression(java_Literal_Expression java_literal_expression) {
        this.java_literal_expression = java_literal_expression;
    }
    public java_Variable_initializer getJava_variable_initializer() {
        return java_variable_initializer;
    }

    public void setJava_variable_initializer(java_Variable_initializer java_variable_initializer) {
        this.java_variable_initializer = java_variable_initializer;
    }

}