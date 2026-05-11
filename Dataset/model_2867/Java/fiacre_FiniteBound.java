





import java.util.List;
import java.util.ArrayList;

public class fiacre_FiniteBound extends MinBound, MaxBound {

    private boolean strict;
    private int val;



    public fiacre_FiniteBound(
        boolean strict,        int val    ) {
        super(
        );
        this.strict = strict;
        this.val = val;
    }


    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }
    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }


}