





import java.util.List;
import java.util.ArrayList;

public class model_change_MergingIssue extends Issue {

    private int resolvingRevision;



    public model_change_MergingIssue(
        int resolvingRevision    ) {
        super(
        );
        this.resolvingRevision = resolvingRevision;
    }


    public int getResolvingrevision() {
        return resolvingRevision;
    }

    public void setResolvingrevision(int resolvingRevision) {
        this.resolvingRevision = resolvingRevision;
    }


}