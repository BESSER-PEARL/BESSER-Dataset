





import java.util.List;
import java.util.ArrayList;

public class gastm_CollectionExpression extends Expression {






    private List<gastm_Expression> gastm_expressions;


    public gastm_CollectionExpression(
    ) {
        super(
        );
        this.gastm_expressions = new ArrayList<>();
    }

    public gastm_CollectionExpression(
        ArrayList<gastm_Expression> gastm_expressions    ) {
        this.gastm_expressions = gastm_expressions;
    }


    public List<gastm_Expression> getGastm_expressions() {
        return gastm_expressions;
    }

    public void addGastm_expression(Gastm_expression gastm_expression) {
        this.gastm_expressions.add(gastm_expression);
    }

}