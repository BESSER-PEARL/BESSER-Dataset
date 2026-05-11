





import java.util.List;
import java.util.ArrayList;

public class relational_CheckConstraint extends TableConstraint {

    private String searchCondition;



    public relational_CheckConstraint(
        String searchCondition    ) {
        super(
        );
        this.searchCondition = searchCondition;
    }


    public String getSearchcondition() {
        return searchCondition;
    }

    public void setSearchcondition(String searchCondition) {
        this.searchCondition = searchCondition;
    }


}