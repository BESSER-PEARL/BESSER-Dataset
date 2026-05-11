





import java.util.List;
import java.util.ArrayList;

public class delphi_relExp extends expression {






    private delphi_expression delphi_expression;




    private delphi_simpleExpression delphi_simpleexpression;


    public delphi_relExp(
    ) {
        super(
        );
    }



    public delphi_expression getDelphi_expression() {
        return delphi_expression;
    }

    public void setDelphi_expression(delphi_expression delphi_expression) {
        this.delphi_expression = delphi_expression;
    }
    public delphi_simpleExpression getDelphi_simpleexpression() {
        return delphi_simpleexpression;
    }

    public void setDelphi_simpleexpression(delphi_simpleExpression delphi_simpleexpression) {
        this.delphi_simpleexpression = delphi_simpleexpression;
    }

}