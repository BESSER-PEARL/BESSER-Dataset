





import java.util.List;
import java.util.ArrayList;

public class java_SingleVariableAccess extends Expression {






    private java_FieldAccess java_fieldaccess;




    private java_Expression java_expression;


    public java_SingleVariableAccess(
    ) {
        super(
        );
    }



    public java_FieldAccess getJava_fieldaccess() {
        return java_fieldaccess;
    }

    public void setJava_fieldaccess(java_FieldAccess java_fieldaccess) {
        this.java_fieldaccess = java_fieldaccess;
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}