





import java.util.List;
import java.util.ArrayList;

public class expression_Predicate extends Expression {

    private boolean negated;



    public expression_Predicate(
        boolean negated    ) {
        super(
        );
        this.negated = negated;
    }


    public boolean getNegated() {
        return negated;
    }

    public void setNegated(boolean negated) {
        this.negated = negated;
    }


}