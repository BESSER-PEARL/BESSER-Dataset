





import java.util.List;
import java.util.ArrayList;

public class astm_FormalParameterDefinition extends DataDefinition {






    private astm_FunctionDefinition astm_functiondefinition;




    private astm_EntryDefinition astm_entrydefinition;


    public astm_FormalParameterDefinition(
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
    public astm_EntryDefinition getAstm_entrydefinition() {
        return astm_entrydefinition;
    }

    public void setAstm_entrydefinition(astm_EntryDefinition astm_entrydefinition) {
        this.astm_entrydefinition = astm_entrydefinition;
    }

}