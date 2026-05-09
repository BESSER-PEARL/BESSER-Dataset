





import java.util.List;
import java.util.ArrayList;

public class JDTAST_FieldAccess extends Expression {






    private JDTAST_SimpleName jdtast_simplename;




    private JDTAST_Expression jdtast_expression;


    public JDTAST_FieldAccess(
    ) {
        super(
        );
    }



    public JDTAST_SimpleName getJdtast_simplename() {
        return jdtast_simplename;
    }

    public void setJdtast_simplename(JDTAST_SimpleName jdtast_simplename) {
        this.jdtast_simplename = jdtast_simplename;
    }
    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }

}