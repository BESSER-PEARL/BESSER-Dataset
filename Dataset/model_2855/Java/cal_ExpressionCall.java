





import java.util.List;
import java.util.ArrayList;

public class cal_ExpressionCall extends AstExpression {






    private cal_Function cal_function;




    private List<cal_AstExpression> cal_astexpressions;




    private List<cal_AstAnnotation> cal_astannotations;


    public cal_ExpressionCall(
    ) {
        super(
        );
        this.cal_astexpressions = new ArrayList<>();
        this.cal_astannotations = new ArrayList<>();
    }

    public cal_ExpressionCall(
        ArrayList<cal_AstExpression> cal_astexpressions,        ArrayList<cal_AstAnnotation> cal_astannotations    ) {
        this.cal_astexpressions = cal_astexpressions;
        this.cal_astannotations = cal_astannotations;
    }


    public cal_Function getCal_function() {
        return cal_function;
    }

    public void setCal_function(cal_Function cal_function) {
        this.cal_function = cal_function;
    }
    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }
    public List<cal_AstAnnotation> getCal_astannotations() {
        return cal_astannotations;
    }

    public void addCal_astannotation(Cal_astannotation cal_astannotation) {
        this.cal_astannotations.add(cal_astannotation);
    }

}