





import java.util.List;
import java.util.ArrayList;

public class ExpressionNode  {






    private smif_expressions_Evaluation smif_expressions_evaluation;




    private smif_expressions_FunctionType smif_expressions_functiontype;


    public ExpressionNode(
    ) {
    }



    public smif_expressions_Evaluation getSmif_expressions_evaluation() {
        return smif_expressions_evaluation;
    }

    public void setSmif_expressions_evaluation(smif_expressions_Evaluation smif_expressions_evaluation) {
        this.smif_expressions_evaluation = smif_expressions_evaluation;
    }
    public smif_expressions_FunctionType getSmif_expressions_functiontype() {
        return smif_expressions_functiontype;
    }

    public void setSmif_expressions_functiontype(smif_expressions_FunctionType smif_expressions_functiontype) {
        this.smif_expressions_functiontype = smif_expressions_functiontype;
    }

}