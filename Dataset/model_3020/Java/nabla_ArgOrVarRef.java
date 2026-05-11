





import java.util.List;
import java.util.ArrayList;

public class nabla_ArgOrVarRef extends Expression {






    private List<nabla_Expression> nabla_expressions;




    private nabla_Affectation nabla_affectation;


    public nabla_ArgOrVarRef(
    ) {
        super(
        );
        this.nabla_expressions = new ArrayList<>();
    }

    public nabla_ArgOrVarRef(
        ArrayList<nabla_Expression> nabla_expressions    ) {
        this.nabla_expressions = nabla_expressions;
    }


    public List<nabla_Expression> getNabla_expressions() {
        return nabla_expressions;
    }

    public void addNabla_expression(Nabla_expression nabla_expression) {
        this.nabla_expressions.add(nabla_expression);
    }
    public nabla_Affectation getNabla_affectation() {
        return nabla_affectation;
    }

    public void setNabla_affectation(nabla_Affectation nabla_affectation) {
        this.nabla_affectation = nabla_affectation;
    }

}