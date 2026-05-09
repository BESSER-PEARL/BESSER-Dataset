





import java.util.List;
import java.util.ArrayList;

public class astm_LabeledStatement extends Statement {






    private astm_Statement astm_statement;




    private astm_LabelDefinition astm_labeldefinition;


    public astm_LabeledStatement(
    ) {
        super(
        );
    }



    public astm_Statement getAstm_statement() {
        return astm_statement;
    }

    public void setAstm_statement(astm_Statement astm_statement) {
        this.astm_statement = astm_statement;
    }
    public astm_LabelDefinition getAstm_labeldefinition() {
        return astm_labeldefinition;
    }

    public void setAstm_labeldefinition(astm_LabelDefinition astm_labeldefinition) {
        this.astm_labeldefinition = astm_labeldefinition;
    }

}