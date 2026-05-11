





import java.util.List;
import java.util.ArrayList;

public class remes_SubMode extends Mode {

    private String invariant;
    private boolean isUrgent;



    public remes_SubMode(
        String invariant,        boolean isUrgent    ) {
        super(
        );
        this.invariant = invariant;
        this.isUrgent = isUrgent;
    }


    public String getInvariant() {
        return invariant;
    }

    public void setInvariant(String invariant) {
        this.invariant = invariant;
    }
    public boolean getIsurgent() {
        return isUrgent;
    }

    public void setIsurgent(boolean isUrgent) {
        this.isUrgent = isUrgent;
    }


}