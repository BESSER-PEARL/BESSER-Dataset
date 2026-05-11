





import java.util.List;
import java.util.ArrayList;

public class pp_UnlessExpression extends Expression {






    private List<pp_Expression> pp_expressions;




    private pp_Expression pp_expression;




    private pp_Expression pp_expression;


    public pp_UnlessExpression(
    ) {
        super(
        );
        this.pp_expressions = new ArrayList<>();
    }

    public pp_UnlessExpression(
        ArrayList<pp_Expression> pp_expressions    ) {
        this.pp_expressions = pp_expressions;
    }


    public List<pp_Expression> getPp_expressions() {
        return pp_expressions;
    }

    public void addPp_expression(Pp_expression pp_expression) {
        this.pp_expressions.add(pp_expression);
    }
    public pp_Expression getPp_expression() {
        return pp_expression;
    }

    public void setPp_expression(pp_Expression pp_expression) {
        this.pp_expression = pp_expression;
    }
    public pp_Expression getPp_expression() {
        return pp_expression;
    }

    public void setPp_expression(pp_Expression pp_expression) {
        this.pp_expression = pp_expression;
    }

}