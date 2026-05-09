





import java.util.List;
import java.util.ArrayList;

public class javaMM_SingleVariableDeclaration extends VariableDeclaration {

    private boolean varargs;





    private javaMM_TypeAccess javamm_typeaccess;


    public javaMM_SingleVariableDeclaration(
        boolean varargs    ) {
        super(
        );
        this.varargs = varargs;
    }


    public boolean getVarargs() {
        return varargs;
    }

    public void setVarargs(boolean varargs) {
        this.varargs = varargs;
    }

    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }

}