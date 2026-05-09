





import java.util.List;
import java.util.ArrayList;

public class javaMM_MethodRefParameter extends ASTNode {

    private String name;
    private String varargs;





    private javaMM_MethodRef javamm_methodref;




    private javaMM_TypeAccess javamm_typeaccess;


    public javaMM_MethodRefParameter(
        String name,        String varargs    ) {
        super(
        );
        this.name = name;
        this.varargs = varargs;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }

    public javaMM_MethodRef getJavamm_methodref() {
        return javamm_methodref;
    }

    public void setJavamm_methodref(javaMM_MethodRef javamm_methodref) {
        this.javamm_methodref = javamm_methodref;
    }
    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }

}