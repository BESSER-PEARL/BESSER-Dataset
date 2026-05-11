





import java.util.List;
import java.util.ArrayList;

public class cool_CaseExpression extends PrimaryExpression {






    private List<cool_Case> cool_cases;




    private cool_Expression cool_expression;


    public cool_CaseExpression(
    ) {
        super(
        );
        this.cool_cases = new ArrayList<>();
    }

    public cool_CaseExpression(
        ArrayList<cool_Case> cool_cases    ) {
        this.cool_cases = cool_cases;
    }


    public List<cool_Case> getCool_cases() {
        return cool_cases;
    }

    public void addCool_case(Cool_case cool_case) {
        this.cool_cases.add(cool_case);
    }
    public cool_Expression getCool_expression() {
        return cool_expression;
    }

    public void setCool_expression(cool_Expression cool_expression) {
        this.cool_expression = cool_expression;
    }

}