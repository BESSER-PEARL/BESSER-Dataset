





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_SynchronizedStatement extends Statement {






    private Block block;




    private Expression expression;


    public JavaAbstractSyntax_SynchronizedStatement(
    ) {
        super(
        );
    }



    public Block getBlock() {
        return block;
    }

    public void setBlock(Block block) {
        this.block = block;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}