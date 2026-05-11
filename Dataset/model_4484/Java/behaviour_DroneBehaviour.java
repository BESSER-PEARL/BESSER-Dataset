





import java.util.List;
import java.util.ArrayList;

public class behaviour_DroneBehaviour extends NamedElement {

    private boolean canBeInterrupted;



    public behaviour_DroneBehaviour(
        boolean canBeInterrupted    ) {
        super(
        );
        this.canBeInterrupted = canBeInterrupted;
    }


    public boolean getCanbeinterrupted() {
        return canBeInterrupted;
    }

    public void setCanbeinterrupted(boolean canBeInterrupted) {
        this.canBeInterrupted = canBeInterrupted;
    }


}