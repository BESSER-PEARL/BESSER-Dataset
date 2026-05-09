





import java.util.List;
import java.util.ArrayList;

public class JDTAST_WhileStatement extends Statement {






    private JDTAST_Expression jdtast_expression;




    private JDTAST_Statement jdtast_statement;


    public JDTAST_WhileStatement(
    ) {
        super(
        );
    }



    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }
    public JDTAST_Statement getJdtast_statement() {
        return jdtast_statement;
    }

    public void setJdtast_statement(JDTAST_Statement jdtast_statement) {
        this.jdtast_statement = jdtast_statement;
    }

}