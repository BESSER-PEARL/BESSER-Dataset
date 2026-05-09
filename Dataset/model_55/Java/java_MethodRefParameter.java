





import java.util.List;
import java.util.ArrayList;

public class java_MethodRefParameter extends ASTNode {

    private boolean varargs;
    private String name;





    private java_MethodRef java_methodref;




    private java_TypeAccess java_typeaccess;


    public java_MethodRefParameter(
        boolean varargs,        String name    ) {
        super(
        );
        this.varargs = varargs;
        this.name = name;
    }


    public boolean getVarargs() {
        return varargs;
    }

    public void setVarargs(boolean varargs) {
        this.varargs = varargs;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public java_MethodRef getJava_methodref() {
        return java_methodref;
    }

    public void setJava_methodref(java_MethodRef java_methodref) {
        this.java_methodref = java_methodref;
    }
    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }

}