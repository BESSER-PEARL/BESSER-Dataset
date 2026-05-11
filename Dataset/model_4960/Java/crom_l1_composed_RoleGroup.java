





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_RoleGroup extends RelationTarget, AbstractRole {

    private int lower;
    private int upper;



    public crom_l1_composed_RoleGroup(
        int lower,        int upper    ) {
        super(
        );
        this.lower = lower;
        this.upper = upper;
    }


    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }


}