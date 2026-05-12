





import java.util.List;
import java.util.ArrayList;

public class javaMM_FieldAccess extends Expression {






    private javaMM_Expression javamm_expression;




    private javaMM_SingleVariableAccess javamm_singlevariableaccess;


    public javaMM_FieldAccess(
    ) {
        super(
        );
    }



    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }
    public javaMM_SingleVariableAccess getJavamm_singlevariableaccess() {
        return javamm_singlevariableaccess;
    }

    public void setJavamm_singlevariableaccess(javaMM_SingleVariableAccess javamm_singlevariableaccess) {
        this.javamm_singlevariableaccess = javamm_singlevariableaccess;
    }

}