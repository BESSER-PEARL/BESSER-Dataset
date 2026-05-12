





import java.util.List;
import java.util.ArrayList;

public class cmt_ProgramCommitteeChair extends ProgramCommitteeMember, Chairman {






    private Review review;


    public cmt_ProgramCommitteeChair(
    ) {
        super(
        );
    }



    public Review getReview() {
        return review;
    }

    public void setReview(Review review) {
        this.review = review;
    }

}