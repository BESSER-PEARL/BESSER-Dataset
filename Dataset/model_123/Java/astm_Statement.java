





import java.util.List;
import java.util.ArrayList;

public class astm_Statement extends GASTMSyntaxObject {






    private astm_CatchBlock astm_catchblock;




    private astm_EntryDefinition astm_entrydefinition;




    private astm_SwitchCase astm_switchcase;




    private astm_FunctionDefinition astm_functiondefinition;


    public astm_Statement(
    ) {
        super(
        );
    }



    public astm_CatchBlock getAstm_catchblock() {
        return astm_catchblock;
    }

    public void setAstm_catchblock(astm_CatchBlock astm_catchblock) {
        this.astm_catchblock = astm_catchblock;
    }
    public astm_EntryDefinition getAstm_entrydefinition() {
        return astm_entrydefinition;
    }

    public void setAstm_entrydefinition(astm_EntryDefinition astm_entrydefinition) {
        this.astm_entrydefinition = astm_entrydefinition;
    }
    public astm_SwitchCase getAstm_switchcase() {
        return astm_switchcase;
    }

    public void setAstm_switchcase(astm_SwitchCase astm_switchcase) {
        this.astm_switchcase = astm_switchcase;
    }
    public astm_FunctionDefinition getAstm_functiondefinition() {
        return astm_functiondefinition;
    }

    public void setAstm_functiondefinition(astm_FunctionDefinition astm_functiondefinition) {
        this.astm_functiondefinition = astm_functiondefinition;
    }

}