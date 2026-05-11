





import java.util.List;
import java.util.ArrayList;

public class model_IntegerRangeLiteralExpression extends LiteralExpression, EnumerableExpression, BinaryExpression {

    private boolean leftInclusive;
    private boolean rightInclusive;



    public model_IntegerRangeLiteralExpression(
        boolean leftInclusive,        boolean rightInclusive    ) {
        super(
        );
        this.leftInclusive = leftInclusive;
        this.rightInclusive = rightInclusive;
    }


    public boolean getLeftinclusive() {
        return leftInclusive;
    }

    public void setLeftinclusive(boolean leftInclusive) {
        this.leftInclusive = leftInclusive;
    }
    public boolean getRightinclusive() {
        return rightInclusive;
    }

    public void setRightinclusive(boolean rightInclusive) {
        this.rightInclusive = rightInclusive;
    }


}