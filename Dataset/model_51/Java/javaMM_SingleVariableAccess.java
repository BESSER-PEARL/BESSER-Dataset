





import java.util.List;
import java.util.ArrayList;

public class javaMM_SingleVariableAccess extends Expression {






    private javaMM_FieldAccess javamm_fieldaccess;




    private javaMM_Expression javamm_expression;


    public javaMM_SingleVariableAccess(
    ) {
        super(
        );
    }



    public javaMM_FieldAccess getJavamm_fieldaccess() {
        return javamm_fieldaccess;
    }

    public void setJavamm_fieldaccess(javaMM_FieldAccess javamm_fieldaccess) {
        this.javamm_fieldaccess = javamm_fieldaccess;
    }
    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }

}