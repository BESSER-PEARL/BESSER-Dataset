





import java.util.List;
import java.util.ArrayList;

public class gastm_ArrayAccess extends Expression {






    private List<gastm_Expression> gastm_expressions;




    private gastm_Expression gastm_expression;


    public gastm_ArrayAccess(
    ) {
        super(
        );
        this.gastm_expressions = new ArrayList<>();
    }

    public gastm_ArrayAccess(
        ArrayList<gastm_Expression> gastm_expressions    ) {
        this.gastm_expressions = gastm_expressions;
    }


    public List<gastm_Expression> getGastm_expressions() {
        return gastm_expressions;
    }

    public void addGastm_expression(Gastm_expression gastm_expression) {
        this.gastm_expressions.add(gastm_expression);
    }
    public gastm_Expression getGastm_expression() {
        return gastm_expression;
    }

    public void setGastm_expression(gastm_Expression gastm_expression) {
        this.gastm_expression = gastm_expression;
    }

}