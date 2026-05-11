





import java.util.List;
import java.util.ArrayList;

public class pp1_ParameterizedExpression extends Expression {






    private pp1_Expression pp1_expression;




    private List<pp1_Expression> pp1_expressions;


    public pp1_ParameterizedExpression(
    ) {
        super(
        );
        this.pp1_expressions = new ArrayList<>();
    }

    public pp1_ParameterizedExpression(
        ArrayList<pp1_Expression> pp1_expressions    ) {
        this.pp1_expressions = pp1_expressions;
    }


    public pp1_Expression getPp1_expression() {
        return pp1_expression;
    }

    public void setPp1_expression(pp1_Expression pp1_expression) {
        this.pp1_expression = pp1_expression;
    }
    public List<pp1_Expression> getPp1_expressions() {
        return pp1_expressions;
    }

    public void addPp1_expression(Pp1_expression pp1_expression) {
        this.pp1_expressions.add(pp1_expression);
    }

}