





import java.util.List;
import java.util.ArrayList;

public class miniJava_IntLiteral extends AbstractExpression {

    private int resultInt;



    public miniJava_IntLiteral(
        int resultInt    ) {
        super(
        );
        this.resultInt = resultInt;
    }


    public int getResultint() {
        return resultInt;
    }

    public void setResultint(int resultInt) {
        this.resultInt = resultInt;
    }


}