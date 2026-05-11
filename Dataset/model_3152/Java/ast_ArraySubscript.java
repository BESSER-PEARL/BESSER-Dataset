





import java.util.List;
import java.util.ArrayList;

public class ast_ArraySubscript  {

    private boolean slice;





    private ast_Expression ast_expression;




    private ast_ArrayElementAccess ast_arrayelementaccess;


    public ast_ArraySubscript(
        boolean slice    ) {
        this.slice = slice;
    }


    public boolean getSlice() {
        return slice;
    }

    public void setSlice(boolean slice) {
        this.slice = slice;
    }

    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public ast_ArrayElementAccess getAst_arrayelementaccess() {
        return ast_arrayelementaccess;
    }

    public void setAst_arrayelementaccess(ast_ArrayElementAccess ast_arrayelementaccess) {
        this.ast_arrayelementaccess = ast_arrayelementaccess;
    }

}