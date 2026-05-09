





import java.util.List;
import java.util.ArrayList;

public class Java_MethodRefParameter extends ASTNode {

    private String name;
    private boolean varargs;



    public Java_MethodRefParameter(
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


}