





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ArrayCreation extends Expression {






    private List<JDTAST_Expression> jdtast_expressions;


    public JDTAST_ArrayCreation(
    ) {
        super(
        );
        this.jdtast_expressions = new ArrayList<>();
    }

    public JDTAST_ArrayCreation(
        ArrayList<JDTAST_Expression> jdtast_expressions    ) {
        this.jdtast_expressions = jdtast_expressions;
    }


    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }

}