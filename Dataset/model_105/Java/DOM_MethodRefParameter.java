





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodRefParameter extends ASTNode {

    private String varargs;



    public DOM_MethodRefParameter(
        String varargs    ) {
        super(
        );
        this.varargs = varargs;
    }


    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }


}