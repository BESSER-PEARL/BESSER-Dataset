





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_AcceptEventAction extends Action {

    private String isUnmarshall;





    private List<uml3_0_0_Trigger> uml3_0_0_triggers;


    public uml3_0_0_AcceptEventAction(
        String isUnmarshall    ) {
        super(
        );
        this.isUnmarshall = isUnmarshall;
        this.uml3_0_0_triggers = new ArrayList<>();
    }

    public uml3_0_0_AcceptEventAction(
        String isUnmarshall        ArrayList<uml3_0_0_Trigger> uml3_0_0_triggers    ) {
        this.isUnmarshall = isUnmarshall;
        this.uml3_0_0_triggers = uml3_0_0_triggers;
    }

    public String getIsunmarshall() {
        return isUnmarshall;
    }

    public void setIsunmarshall(String isUnmarshall) {
        this.isUnmarshall = isUnmarshall;
    }

    public List<uml3_0_0_Trigger> getUml3_0_0_triggers() {
        return uml3_0_0_triggers;
    }

    public void addUml3_0_0_trigger(Uml3_0_0_trigger uml3_0_0_trigger) {
        this.uml3_0_0_triggers.add(uml3_0_0_trigger);
    }

}