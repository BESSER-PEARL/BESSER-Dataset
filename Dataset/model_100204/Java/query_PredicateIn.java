





import java.util.List;
import java.util.ArrayList;

public class query_PredicateIn extends Predicate {

    private boolean notIn;



    public query_PredicateIn(
        boolean notIn    ) {
        super(
        );
        this.notIn = notIn;
    }


    public boolean getNotin() {
        return notIn;
    }

    public void setNotin(boolean notIn) {
        this.notIn = notIn;
    }


}