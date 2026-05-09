





import java.util.List;
import java.util.ArrayList;

public class DOM_SynchronizedStatement extends Statement {






    private Expression expression;




    private Block block;


    public DOM_SynchronizedStatement(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public Block getBlock() {
        return block;
    }

    public void setBlock(Block block) {
        this.block = block;
    }

}