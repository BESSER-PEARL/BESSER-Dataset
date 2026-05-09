





import java.util.List;
import java.util.ArrayList;

public class JDTAST_SuperMethodInvocation extends Expression {






    private JDTAST_Name jdtast_name;




    private JDTAST_Name jdtast_name;




    private List<JDTAST_Expression> jdtast_expressions;




    private List<JDTAST_Type> jdtast_types;


    public JDTAST_SuperMethodInvocation(
    ) {
        super(
        );
        this.jdtast_expressions = new ArrayList<>();
        this.jdtast_types = new ArrayList<>();
    }

    public JDTAST_SuperMethodInvocation(
        ArrayList<JDTAST_Expression> jdtast_expressions,        ArrayList<JDTAST_Type> jdtast_types    ) {
        this.jdtast_expressions = jdtast_expressions;
        this.jdtast_types = jdtast_types;
    }


    public JDTAST_Name getJdtast_name() {
        return jdtast_name;
    }

    public void setJdtast_name(JDTAST_Name jdtast_name) {
        this.jdtast_name = jdtast_name;
    }
    public JDTAST_Name getJdtast_name() {
        return jdtast_name;
    }

    public void setJdtast_name(JDTAST_Name jdtast_name) {
        this.jdtast_name = jdtast_name;
    }
    public List<JDTAST_Expression> getJdtast_expressions() {
        return jdtast_expressions;
    }

    public void addJdtast_expression(Jdtast_expression jdtast_expression) {
        this.jdtast_expressions.add(jdtast_expression);
    }
    public List<JDTAST_Type> getJdtast_types() {
        return jdtast_types;
    }

    public void addJdtast_type(Jdtast_type jdtast_type) {
        this.jdtast_types.add(jdtast_type);
    }

}