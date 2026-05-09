





import java.util.List;
import java.util.ArrayList;

public class JDTAST_MethodRefParameter extends ASTNode {

    private String varargs;





    private JDTAST_MethodRef jdtast_methodref;


    public JDTAST_MethodRefParameter(
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

    public JDTAST_MethodRef getJdtast_methodref() {
        return jdtast_methodref;
    }

    public void setJdtast_methodref(JDTAST_MethodRef jdtast_methodref) {
        this.jdtast_methodref = jdtast_methodref;
    }

}