





import java.util.List;
import java.util.ArrayList;

public class pp_CaseExpression extends Expression {






    private pp_Expression pp_expression;




    private List<pp_Case> pp_cases;


    public pp_CaseExpression(
    ) {
        super(
        );
        this.pp_cases = new ArrayList<>();
    }

    public pp_CaseExpression(
        ArrayList<pp_Case> pp_cases    ) {
        this.pp_cases = pp_cases;
    }


    public pp_Expression getPp_expression() {
        return pp_expression;
    }

    public void setPp_expression(pp_Expression pp_expression) {
        this.pp_expression = pp_expression;
    }
    public List<pp_Case> getPp_cases() {
        return pp_cases;
    }

    public void addPp_case(Pp_case pp_case) {
        this.pp_cases.add(pp_case);
    }

}