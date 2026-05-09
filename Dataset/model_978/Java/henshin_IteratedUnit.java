





import java.util.List;
import java.util.ArrayList;

public class henshin_IteratedUnit extends UnaryUnit {

    private boolean rollback;
    private String iterations;
    private boolean strict;



    public henshin_IteratedUnit(
        boolean rollback,        String iterations,        boolean strict    ) {
        super(
        );
        this.rollback = rollback;
        this.iterations = iterations;
        this.strict = strict;
    }


    public boolean getRollback() {
        return rollback;
    }

    public void setRollback(boolean rollback) {
        this.rollback = rollback;
    }
    public String getIterations() {
        return iterations;
    }

    public void setIterations(String iterations) {
        this.iterations = iterations;
    }
    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }


}