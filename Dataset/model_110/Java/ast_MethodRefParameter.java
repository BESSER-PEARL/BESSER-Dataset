





import java.util.List;
import java.util.ArrayList;

public class ast_MethodRefParameter extends ASTNode {

    private boolean varargs;





    private ast_SimpleName ast_simplename;




    private ast_MethodRef ast_methodref;


    public ast_MethodRefParameter(
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

    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public ast_MethodRef getAst_methodref() {
        return ast_methodref;
    }

    public void setAst_methodref(ast_MethodRef ast_methodref) {
        this.ast_methodref = ast_methodref;
    }

}