





import java.util.List;
import java.util.ArrayList;

public class Actions_CompleteActions_AcceptEventAction extends Action {

    private boolean isUnmarshall;





    private List<Trigger> triggers;


    public Actions_CompleteActions_AcceptEventAction(
        boolean isUnmarshall    ) {
        super(
        );
        this.isUnmarshall = isUnmarshall;
        this.triggers = new ArrayList<>();
    }

    public Actions_CompleteActions_AcceptEventAction(
        boolean isUnmarshall        ArrayList<Trigger> triggers    ) {
        this.isUnmarshall = isUnmarshall;
        this.triggers = triggers;
    }

    public boolean getIsunmarshall() {
        return isUnmarshall;
    }

    public void setIsunmarshall(boolean isUnmarshall) {
        this.isUnmarshall = isUnmarshall;
    }

    public List<Trigger> getTriggers() {
        return triggers;
    }

    public void addTrigger(Trigger trigger) {
        this.triggers.add(trigger);
    }

}