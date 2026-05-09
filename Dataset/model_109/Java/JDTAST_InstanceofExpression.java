





import java.util.List;
import java.util.ArrayList;

public class JDTAST_InstanceofExpression extends Expression {






    private JDTAST_Type jdtast_type;




    private JDTAST_Expression jdtast_expression;


    public JDTAST_InstanceofExpression(
    ) {
        super(
        );
    }



    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }
    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }

}