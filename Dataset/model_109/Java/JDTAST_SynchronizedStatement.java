





import java.util.List;
import java.util.ArrayList;

public class JDTAST_SynchronizedStatement extends Statement {






    private JDTAST_Expression jdtast_expression;




    private JDTAST_Block jdtast_block;


    public JDTAST_SynchronizedStatement(
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
    public JDTAST_Block getJdtast_block() {
        return jdtast_block;
    }

    public void setJdtast_block(JDTAST_Block jdtast_block) {
        this.jdtast_block = jdtast_block;
    }

}