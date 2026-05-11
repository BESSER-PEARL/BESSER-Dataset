





import java.util.List;
import java.util.ArrayList;

public class vql_PatternCompositionConstraint extends Constraint {

    private boolean negative;



    public vql_PatternCompositionConstraint(
        boolean negative    ) {
        super(
        );
        this.negative = negative;
    }


    public boolean getNegative() {
        return negative;
    }

    public void setNegative(boolean negative) {
        this.negative = negative;
    }


}