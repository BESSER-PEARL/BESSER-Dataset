





import java.util.List;
import java.util.ArrayList;

public class ast_ArrayConstructionIterationClause  {

    private String variableName;





    private ast_Expression ast_expression;




    private ast_ArrayConstructionOperator ast_arrayconstructionoperator;


    public ast_ArrayConstructionIterationClause(
        String variableName    ) {
        this.variableName = variableName;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }

    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public ast_ArrayConstructionOperator getAst_arrayconstructionoperator() {
        return ast_arrayconstructionoperator;
    }

    public void setAst_arrayconstructionoperator(ast_ArrayConstructionOperator ast_arrayconstructionoperator) {
        this.ast_arrayconstructionoperator = ast_arrayconstructionoperator;
    }

}