





import java.util.List;
import java.util.ArrayList;

public class reviews_ReviewItemSet extends ReviewItem, Dated {

    private String revision;
    private boolean inNeedOfRetrieval;



    public reviews_ReviewItemSet(
        String revision,        boolean inNeedOfRetrieval    ) {
        super(
        );
        this.revision = revision;
        this.inNeedOfRetrieval = inNeedOfRetrieval;
    }


    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }
    public boolean getInneedofretrieval() {
        return inNeedOfRetrieval;
    }

    public void setInneedofretrieval(boolean inNeedOfRetrieval) {
        this.inNeedOfRetrieval = inNeedOfRetrieval;
    }


}