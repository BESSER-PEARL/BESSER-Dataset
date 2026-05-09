





import java.util.List;
import java.util.ArrayList;

public class javaMM_ClassInstanceCreation extends Expression, AbstractMethodInvocation {






    private javaMM_TypeAccess javamm_typeaccess;




    private javaMM_Expression javamm_expression;


    public javaMM_ClassInstanceCreation(
    ) {
        super(
        );
    }



    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }

}