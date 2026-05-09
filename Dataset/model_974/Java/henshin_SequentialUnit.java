





import java.util.List;
import java.util.ArrayList;

public class henshin_SequentialUnit extends MultiUnit {

    private boolean rollback;
    private boolean strict;



    public henshin_SequentialUnit(
        boolean rollback,        boolean strict    ) {
        super(
        );
        this.rollback = rollback;
        this.strict = strict;
    }


    public boolean getRollback() {
        return rollback;
    }

    public void setRollback(boolean rollback) {
        this.rollback = rollback;
    }
    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }


}