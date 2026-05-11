





import java.util.List;
import java.util.ArrayList;

public class sADL_ExpressionStatement extends ExpressionScope {

    private String evaluatesTo;





    private sADL_Expression sadl_expression;


    public sADL_ExpressionStatement(
        String evaluatesTo    ) {
        super(
        );
        this.evaluatesTo = evaluatesTo;
    }


    public String getEvaluatesto() {
        return evaluatesTo;
    }

    public void setEvaluatesto(String evaluatesTo) {
        this.evaluatesTo = evaluatesTo;
    }

    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }

}