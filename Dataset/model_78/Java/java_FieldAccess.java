





import java.util.List;
import java.util.ArrayList;

public class java_FieldAccess extends Expression {






    private java_SingleVariableAccess java_singlevariableaccess;




    private java_Expression java_expression;


    public java_FieldAccess(
    ) {
        super(
        );
    }



    public java_SingleVariableAccess getJava_singlevariableaccess() {
        return java_singlevariableaccess;
    }

    public void setJava_singlevariableaccess(java_SingleVariableAccess java_singlevariableaccess) {
        this.java_singlevariableaccess = java_singlevariableaccess;
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}