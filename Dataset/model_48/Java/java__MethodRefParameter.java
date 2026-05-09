





import java.util.List;
import java.util.ArrayList;

public class java__MethodRefParameter extends ASTNode {

    private String name;
    private boolean varargs;





    private java__MethodRef java__methodref;




    private java__TypeAccess java__typeaccess;


    public java__MethodRefParameter(
        String name,        boolean varargs    ) {
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
    public boolean getVarargs() {
        return varargs;
    }

    public void setVarargs(boolean varargs) {
        this.varargs = varargs;
    }

    public java__MethodRef getJava__methodref() {
        return java__methodref;
    }

    public void setJava__methodref(java__MethodRef java__methodref) {
        this.java__methodref = java__methodref;
    }
    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }

}