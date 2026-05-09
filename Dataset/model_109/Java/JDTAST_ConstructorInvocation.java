





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ConstructorInvocation extends Statement {






    private List<JDTAST_Type> jdtast_types;




    private List<JDTAST_Expression> jdtast_expressions;


    public JDTAST_ConstructorInvocation(
    ) {
        super(
        );
        this.jdtast_types = new ArrayList<>();
        this.jdtast_expressions = new ArrayList<>();
    }

    public JDTAST_ConstructorInvocation(
        ArrayList<JDTAST_Type> jdtast_types,        ArrayList<JDTAST_Expression> jdtast_expressions    ) {
        this.jdtast_types = jdtast_types;
        this.jdtast_expressions = jdtast_expressions;
    }


    public List<JDTAST_Type> getJdtast_types() {
        return jdtast_types;
    }

    public void addJdtast_type(Jdtast_type jdtast_type) {
        this.jdtast_types.add(jdtast_type);
    }
    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }

}