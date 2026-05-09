





import java.util.List;
import java.util.ArrayList;

public class javaDsl_SynchronizedStatement extends Statement {






    private javaDsl_Expression javadsl_expression;




    private javaDsl_Block javadsl_block;


    public javaDsl_SynchronizedStatement(
    ) {
        super(
        );
    }



    public javaDsl_Expression getJavadsl_expression() {
        return javadsl_expression;
    }

    public void setJavadsl_expression(javaDsl_Expression javadsl_expression) {
        this.javadsl_expression = javadsl_expression;
    }
    public javaDsl_Block getJavadsl_block() {
        return javadsl_block;
    }

    public void setJavadsl_block(javaDsl_Block javadsl_block) {
        this.javadsl_block = javadsl_block;
    }

}