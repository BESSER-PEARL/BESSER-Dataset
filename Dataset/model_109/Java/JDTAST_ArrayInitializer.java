





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ArrayInitializer extends Expression {






    private List<JDTAST_Expression> jdtast_expressions;




    private JDTAST_ArrayCreation jdtast_arraycreation;


    public JDTAST_ArrayInitializer(
    ) {
        super(
        );
        this.jdtast_expressions = new ArrayList<>();
    }

    public JDTAST_ArrayInitializer(
        ArrayList<JDTAST_Expression> jdtast_expressions    ) {
        this.jdtast_expressions = jdtast_expressions;
    }


    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }
    public JDTAST_ArrayCreation getJdtast_arraycreation() {
        return jdtast_arraycreation;
    }

    public void setJdtast_arraycreation(JDTAST_ArrayCreation jdtast_arraycreation) {
        this.jdtast_arraycreation = jdtast_arraycreation;
    }

}