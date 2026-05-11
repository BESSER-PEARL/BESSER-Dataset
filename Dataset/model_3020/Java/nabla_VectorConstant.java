





import java.util.List;
import java.util.ArrayList;

public class nabla_VectorConstant extends Expression {






    private List<nabla_Expression> nabla_expressions;


    public nabla_VectorConstant(
    ) {
        super(
        );
        this.nabla_expressions = new ArrayList<>();
    }

    public nabla_VectorConstant(
        ArrayList<nabla_Expression> nabla_expressions    ) {
        this.nabla_expressions = nabla_expressions;
    }


    public List<nabla_Expression> getNabla_expressions() {
        return nabla_expressions;
    }

    public void addNabla_expression(Nabla_expression nabla_expression) {
        this.nabla_expressions.add(nabla_expression);
    }

}