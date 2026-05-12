





import java.util.List;
import java.util.ArrayList;

public class cmt_Administrator extends User {






    private Reviewer reviewer;


    public cmt_Administrator(
    ) {
        super(
        );
    }



    public Reviewer getReviewer() {
        return reviewer;
    }

    public void setReviewer(Reviewer reviewer) {
        this.reviewer = reviewer;
    }

}