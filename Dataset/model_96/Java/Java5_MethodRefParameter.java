





import java.util.List;
import java.util.ArrayList;

public class Java5_MethodRefParameter extends ASTNode {

    private String name;
    private String isVarargs;





    private Java5_MethodRef java5_methodref;


    public Java5_MethodRefParameter(
        String name,        String isVarargs    ) {
        super(
        );
        this.name = name;
        this.isVarargs = isVarargs;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsvarargs() {
        return isVarargs;
    }

    public void setIsvarargs(String isVarargs) {
        this.isVarargs = isVarargs;
    }

    public Java5_MethodRef getJava5_methodref() {
        return java5_methodref;
    }

    public void setJava5_methodref(Java5_MethodRef java5_methodref) {
        this.java5_methodref = java5_methodref;
    }

}