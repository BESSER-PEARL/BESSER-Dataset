





import java.util.List;
import java.util.ArrayList;

public class pn_Net extends NamedElement {

    private String incrementalID;



    public pn_Net(
        String incrementalID    ) {
        super(
        );
        this.incrementalID = incrementalID;
    }


    public String getIncrementalid() {
        return incrementalID;
    }

    public void setIncrementalid(String incrementalID) {
        this.incrementalID = incrementalID;
    }


}