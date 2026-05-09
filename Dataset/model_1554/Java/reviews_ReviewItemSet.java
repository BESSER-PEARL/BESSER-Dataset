





import java.util.List;
import java.util.ArrayList;

public class reviews_ReviewItemSet extends Dated, ReviewItem {

    private String revision;



    public reviews_ReviewItemSet(
        String revision    ) {
        super(
        );
        this.revision = revision;
    }


    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }


}