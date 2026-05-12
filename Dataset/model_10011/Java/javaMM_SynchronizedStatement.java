





import java.util.List;
import java.util.ArrayList;

public class javaMM_SynchronizedStatement extends Statement {






    private javaMM_Expression javamm_expression;




    private javaMM_Block javamm_block;


    public javaMM_SynchronizedStatement(
    ) {
        super(
        );
    }



    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }
    public javaMM_Block getJavamm_block() {
        return javamm_block;
    }

    public void setJavamm_block(javaMM_Block javamm_block) {
        this.javamm_block = javamm_block;
    }

}