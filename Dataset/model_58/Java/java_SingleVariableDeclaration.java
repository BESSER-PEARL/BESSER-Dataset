





import java.util.List;
import java.util.ArrayList;

public class java_SingleVariableDeclaration extends VariableDeclaration {

    private boolean varargs;



    public java_SingleVariableDeclaration(
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


}