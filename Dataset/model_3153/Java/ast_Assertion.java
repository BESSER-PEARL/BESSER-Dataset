





import java.util.List;
import java.util.ArrayList;

public class ast_Assertion  {

    private String statusKind;
    private boolean static;





    private ast_FunctionDefinition ast_functiondefinition;


    public ast_Assertion(
        String statusKind,        boolean static    ) {
        this.statusKind = statusKind;
        this.static = static;
    }


    public String getStatuskind() {
        return statusKind;
    }

    public void setStatuskind(String statusKind) {
        this.statusKind = statusKind;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public ast_FunctionDefinition getAst_functiondefinition() {
        return ast_functiondefinition;
    }

    public void setAst_functiondefinition(ast_FunctionDefinition ast_functiondefinition) {
        this.ast_functiondefinition = ast_functiondefinition;
    }

}