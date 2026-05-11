





import java.util.List;
import java.util.ArrayList;

public class ast_StepExpression  {






    private ast_VariableAccess ast_variableaccess;




    private ast_NegateStepExpression ast_negatestepexpression;


    public ast_StepExpression(
    ) {
    }



    public ast_VariableAccess getAst_variableaccess() {
        return ast_variableaccess;
    }

    public void setAst_variableaccess(ast_VariableAccess ast_variableaccess) {
        this.ast_variableaccess = ast_variableaccess;
    }
    public ast_NegateStepExpression getAst_negatestepexpression() {
        return ast_negatestepexpression;
    }

    public void setAst_negatestepexpression(ast_NegateStepExpression ast_negatestepexpression) {
        this.ast_negatestepexpression = ast_negatestepexpression;
    }

}