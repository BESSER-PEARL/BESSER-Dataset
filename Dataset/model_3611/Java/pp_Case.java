





import java.util.List;
import java.util.ArrayList;

public class pp_Case  {






    private pp_CaseExpression pp_caseexpression;




    private List<pp_Expression> pp_expressions;




    private List<pp_Expression> pp_expressions;


    public pp_Case(
    ) {
        this.pp_expressions = new ArrayList<>();
        this.pp_expressions = new ArrayList<>();
    }

    public pp_Case(
        ArrayList<pp_Expression> pp_expressions,        ArrayList<pp_Expression> pp_expressions    ) {
        this.pp_expressions = pp_expressions;
        this.pp_expressions = pp_expressions;
    }


    public pp_CaseExpression getPp_caseexpression() {
        return pp_caseexpression;
    }

    public void setPp_caseexpression(pp_CaseExpression pp_caseexpression) {
        this.pp_caseexpression = pp_caseexpression;
    }
    public List<pp_Expression> getPp_expressions() {
        return pp_expressions;
    }

    public void addPp_expression(Pp_expression pp_expression) {
        this.pp_expressions.add(pp_expression);
    }
    public List<pp_Expression> getPp_expressions() {
        return pp_expressions;
    }

    public void addPp_expression(Pp_expression pp_expression) {
        this.pp_expressions.add(pp_expression);
    }

}