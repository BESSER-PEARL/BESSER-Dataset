





import java.util.List;
import java.util.ArrayList;

public class astm_RDBModifyStatement extends Statement {






    private astm_Expression astm_expression;




    private List<astm_NameSpaceDefinition> astm_namespacedefinitions;


    public astm_RDBModifyStatement(
    ) {
        super(
        );
        this.astm_namespacedefinitions = new ArrayList<>();
    }

    public astm_RDBModifyStatement(
        ArrayList<astm_NameSpaceDefinition> astm_namespacedefinitions    ) {
        this.astm_namespacedefinitions = astm_namespacedefinitions;
    }


    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }
    public List<astm_NameSpaceDefinition> getAstm_namespacedefinitions() {
        return astm_namespacedefinitions;
    }

    public void addAstm_namespacedefinition(Astm_namespacedefinition astm_namespacedefinition) {
        this.astm_namespacedefinitions.add(astm_namespacedefinition);
    }

}