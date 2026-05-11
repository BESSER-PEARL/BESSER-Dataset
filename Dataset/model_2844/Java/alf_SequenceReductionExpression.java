





import java.util.List;
import java.util.ArrayList;

public class alf_SequenceReductionExpression extends SuffixExpression {

    private boolean isOrdered;



    public alf_SequenceReductionExpression(
        boolean isOrdered    ) {
        super(
        );
        this.isOrdered = isOrdered;
    }


    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }


}