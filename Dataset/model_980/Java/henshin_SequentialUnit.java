





import java.util.List;
import java.util.ArrayList;

public class henshin_SequentialUnit extends MultiUnit {

    private boolean strict;
    private boolean rollback;



    public henshin_SequentialUnit(
        boolean strict,        boolean rollback    ) {
        super(
        );
        this.strict = strict;
        this.rollback = rollback;
    }


    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }
    public boolean getRollback() {
        return rollback;
    }

    public void setRollback(boolean rollback) {
        this.rollback = rollback;
    }


}