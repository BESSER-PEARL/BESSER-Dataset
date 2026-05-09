





import java.util.List;
import java.util.ArrayList;

public class Java_SingleVariableAccess extends Expression {






    private Java_FieldAccess java_fieldaccess;




    private Java_Expression java_expression;


    public Java_SingleVariableAccess(
    ) {
        super(
        );
    }



    public Java_FieldAccess getJava_fieldaccess() {
        return java_fieldaccess;
    }

    public void setJava_fieldaccess(Java_FieldAccess java_fieldaccess) {
        this.java_fieldaccess = java_fieldaccess;
    }
    public Java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(Java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}