





import java.util.List;
import java.util.ArrayList;

public class sml_WaitCondition extends Condition {

    private boolean requested;
    private boolean strict;



    public sml_WaitCondition(
        boolean requested,        boolean strict    ) {
        super(
        );
        this.requested = requested;
        this.strict = strict;
    }


    public boolean getRequested() {
        return requested;
    }

    public void setRequested(boolean requested) {
        this.requested = requested;
    }
    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }


}