





import java.util.List;
import java.util.ArrayList;

public class java_MethodRefParameter extends ASTNode {

    private boolean varargs;
    private String name;



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


}