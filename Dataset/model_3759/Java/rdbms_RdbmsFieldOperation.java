





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsFieldOperation extends RdbmsElement {

    private boolean reviewRequired;



    public rdbms_RdbmsFieldOperation(
        boolean reviewRequired    ) {
        super(
        );
        this.reviewRequired = reviewRequired;
    }


    public boolean getReviewrequired() {
        return reviewRequired;
    }

    public void setReviewrequired(boolean reviewRequired) {
        this.reviewRequired = reviewRequired;
    }


}