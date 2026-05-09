





import java.util.List;
import java.util.ArrayList;

public class astm_RDBTableReference extends IdentifierReference {






    private astm_RDBRefIntegrity astm_rdbrefintegrity;




    private astm_RDBSelectExpression astm_rdbselectexpression;




    private astm_LabelDefinition astm_labeldefinition;


    public astm_RDBTableReference(
    ) {
        super(
        );
    }



    public astm_RDBRefIntegrity getAstm_rdbrefintegrity() {
        return astm_rdbrefintegrity;
    }

    public void setAstm_rdbrefintegrity(astm_RDBRefIntegrity astm_rdbrefintegrity) {
        this.astm_rdbrefintegrity = astm_rdbrefintegrity;
    }
    public astm_RDBSelectExpression getAstm_rdbselectexpression() {
        return astm_rdbselectexpression;
    }

    public void setAstm_rdbselectexpression(astm_RDBSelectExpression astm_rdbselectexpression) {
        this.astm_rdbselectexpression = astm_rdbselectexpression;
    }
    public astm_LabelDefinition getAstm_labeldefinition() {
        return astm_labeldefinition;
    }

    public void setAstm_labeldefinition(astm_LabelDefinition astm_labeldefinition) {
        this.astm_labeldefinition = astm_labeldefinition;
    }

}