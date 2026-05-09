





import java.util.List;
import java.util.ArrayList;

public class javaMM_ArrayInitializer extends Expression {






    private javaMM_ArrayCreation javamm_arraycreation;




    private List<javaMM_Expression> javamm_expressions;


    public javaMM_ArrayInitializer(
    ) {
        super(
        );
        this.javamm_expressions = new ArrayList<>();
    }

    public javaMM_ArrayInitializer(
        ArrayList<javaMM_Expression> javamm_expressions    ) {
        this.javamm_expressions = javamm_expressions;
    }


    public javaMM_ArrayCreation getJavamm_arraycreation() {
        return javamm_arraycreation;
    }

    public void setJavamm_arraycreation(javaMM_ArrayCreation javamm_arraycreation) {
        this.javamm_arraycreation = javamm_arraycreation;
    }
    public List<javaMM_Expression> getJavamm_expressions() {
        return javamm_expressions;
    }

    public void addJavamm_expression(Javamm_expression javamm_expression) {
        this.javamm_expressions.add(javamm_expression);
    }

}