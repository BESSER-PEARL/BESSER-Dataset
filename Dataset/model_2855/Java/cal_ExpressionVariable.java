





import java.util.List;
import java.util.ArrayList;

public class cal_ExpressionVariable extends AstExpression {






    private cal_VariableReference cal_variablereference;


    public cal_ExpressionVariable(
    ) {
        super(
        );
    }



    public cal_VariableReference getCal_variablereference() {
        return cal_variablereference;
    }

    public void setCal_variablereference(cal_VariableReference cal_variablereference) {
        this.cal_variablereference = cal_variablereference;
    }

}