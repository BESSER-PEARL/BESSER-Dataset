





import java.util.List;
import java.util.ArrayList;

public class ast_InputParameterDeclaration extends ParameterDeclaration {






    private ast_FunctionDefinition ast_functiondefinition;


    public ast_InputParameterDeclaration(
    ) {
        super(
        );
    }



    public ast_FunctionDefinition getAst_functiondefinition() {
        return ast_functiondefinition;
    }

    public void setAst_functiondefinition(ast_FunctionDefinition ast_functiondefinition) {
        this.ast_functiondefinition = ast_functiondefinition;
    }

}