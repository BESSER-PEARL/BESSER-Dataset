





import java.util.List;
import java.util.ArrayList;

public class query_Predicate extends QuerySearchCondition {

    private boolean hasSelectivity;
    private String selectivityValue;
    private boolean negatedPredicate;



    public query_Predicate(
        boolean hasSelectivity,        String selectivityValue,        boolean negatedPredicate    ) {
        super(
        );
        this.hasSelectivity = hasSelectivity;
        this.selectivityValue = selectivityValue;
        this.negatedPredicate = negatedPredicate;
    }


    public boolean getHasselectivity() {
        return hasSelectivity;
    }

    public void setHasselectivity(boolean hasSelectivity) {
        this.hasSelectivity = hasSelectivity;
    }
    public String getSelectivityvalue() {
        return selectivityValue;
    }

    public void setSelectivityvalue(String selectivityValue) {
        this.selectivityValue = selectivityValue;
    }
    public boolean getNegatedpredicate() {
        return negatedPredicate;
    }

    public void setNegatedpredicate(boolean negatedPredicate) {
        this.negatedPredicate = negatedPredicate;
    }


}