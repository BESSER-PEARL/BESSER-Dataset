





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_constraints_CheckConstraint extends TableConstraint {






    private SearchCondition searchcondition;


    public sqlmodel_constraints_CheckConstraint(
    ) {
        super(
        );
    }



    public SearchCondition getSearchcondition() {
        return searchcondition;
    }

    public void setSearchcondition(SearchCondition searchcondition) {
        this.searchcondition = searchcondition;
    }

}