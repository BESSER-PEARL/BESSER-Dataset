





import java.util.List;
import java.util.ArrayList;

public class delphi_exprList extends CSTrace {






    private List<delphi_expression> delphi_expressions;




    private delphi_factor delphi_factor;


    public delphi_exprList(
    ) {
        super(
        );
        this.delphi_expressions = new ArrayList<>();
    }

    public delphi_exprList(
        ArrayList<delphi_expression> delphi_expressions    ) {
        this.delphi_expressions = delphi_expressions;
    }


    public List<delphi_expression> getDelphi_expressions() {
        return delphi_expressions;
    }

    public void addDelphi_expression(Delphi_expression delphi_expression) {
        this.delphi_expressions.add(delphi_expression);
    }
    public delphi_factor getDelphi_factor() {
        return delphi_factor;
    }

    public void setDelphi_factor(delphi_factor delphi_factor) {
        this.delphi_factor = delphi_factor;
    }

}