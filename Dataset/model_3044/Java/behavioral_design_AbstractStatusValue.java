





import java.util.List;
import java.util.ArrayList;

public class behavioral_design_AbstractStatusValue extends NamedElement {

    private boolean isInhibiting;
    private boolean isStateGuarded;
    private boolean isInitial;



    public behavioral_design_AbstractStatusValue(
        boolean isInhibiting,        boolean isStateGuarded,        boolean isInitial    ) {
        super(
        );
        this.isInhibiting = isInhibiting;
        this.isStateGuarded = isStateGuarded;
        this.isInitial = isInitial;
    }


    public boolean getIsinhibiting() {
        return isInhibiting;
    }

    public void setIsinhibiting(boolean isInhibiting) {
        this.isInhibiting = isInhibiting;
    }
    public boolean getIsstateguarded() {
        return isStateGuarded;
    }

    public void setIsstateguarded(boolean isStateGuarded) {
        this.isStateGuarded = isStateGuarded;
    }
    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }


}