





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_RoleGroup extends AbstractRole, RelationTarget {

    private int upper;
    private int lower;



    public crom_l1_composed_RoleGroup(
        int upper,        int lower    ) {
        super(
        );
        this.upper = upper;
        this.lower = lower;
    }


    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }


}