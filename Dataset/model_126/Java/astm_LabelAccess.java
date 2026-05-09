





import java.util.List;
import java.util.ArrayList;

public class astm_LabelAccess extends Expression {






    private astm_Name astm_name;




    private astm_LabelDefinition astm_labeldefinition;




    private astm_ContinueStatement astm_continuestatement;




    private astm_BreakStatement astm_breakstatement;


    public astm_LabelAccess(
    ) {
        super(
        );
    }



    public astm_Name getAstm_name() {
        return astm_name;
    }

    public void setAstm_name(astm_Name astm_name) {
        this.astm_name = astm_name;
    }
    public astm_LabelDefinition getAstm_labeldefinition() {
        return astm_labeldefinition;
    }

    public void setAstm_labeldefinition(astm_LabelDefinition astm_labeldefinition) {
        this.astm_labeldefinition = astm_labeldefinition;
    }
    public astm_ContinueStatement getAstm_continuestatement() {
        return astm_continuestatement;
    }

    public void setAstm_continuestatement(astm_ContinueStatement astm_continuestatement) {
        this.astm_continuestatement = astm_continuestatement;
    }
    public astm_BreakStatement getAstm_breakstatement() {
        return astm_breakstatement;
    }

    public void setAstm_breakstatement(astm_BreakStatement astm_breakstatement) {
        this.astm_breakstatement = astm_breakstatement;
    }

}