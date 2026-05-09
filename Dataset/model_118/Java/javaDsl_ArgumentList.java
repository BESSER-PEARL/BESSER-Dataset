





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ArgumentList  {






    private List<javaDsl_Expression> javadsl_expressions;




    private javaDsl_ExplicitConstructorInvocation javadsl_explicitconstructorinvocation;


    public javaDsl_ArgumentList(
    ) {
        this.javadsl_expressions = new ArrayList<>();
    }

    public javaDsl_ArgumentList(
        ArrayList<javaDsl_Expression> javadsl_expressions    ) {
        this.javadsl_expressions = javadsl_expressions;
    }


    public List<javaDsl_Expression> getJavadsl_expressions() {
        return javadsl_expressions;
    }

    public void addJavadsl_expression(Javadsl_expression javadsl_expression) {
        this.javadsl_expressions.add(javadsl_expression);
    }
    public javaDsl_ExplicitConstructorInvocation getJavadsl_explicitconstructorinvocation() {
        return javadsl_explicitconstructorinvocation;
    }

    public void setJavadsl_explicitconstructorinvocation(javaDsl_ExplicitConstructorInvocation javadsl_explicitconstructorinvocation) {
        this.javadsl_explicitconstructorinvocation = javadsl_explicitconstructorinvocation;
    }

}