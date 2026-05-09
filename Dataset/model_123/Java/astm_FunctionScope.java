





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionScope extends Scope {






    private astm_FunctionDefinition astm_functiondefinition;


    public astm_FunctionScope(
    ) {
        super(
        );
    }



    public astm_FunctionDefinition getAstm_functiondefinition() {
        return astm_functiondefinition;
    }

    public void setAstm_functiondefinition(astm_FunctionDefinition astm_functiondefinition) {
        this.astm_functiondefinition = astm_functiondefinition;
    }

}