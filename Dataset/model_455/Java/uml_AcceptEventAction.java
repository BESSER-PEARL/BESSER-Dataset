





import java.util.List;
import java.util.ArrayList;

public class uml_AcceptEventAction extends Action {

    private String isUnmarshall;





    private List<uml_Trigger> uml_triggers;


    public uml_AcceptEventAction(
        String isUnmarshall    ) {
        super(
        );
        this.isUnmarshall = isUnmarshall;
        this.uml_triggers = new ArrayList<>();
    }

    public uml_AcceptEventAction(
        String isUnmarshall        ArrayList<uml_Trigger> uml_triggers    ) {
        this.isUnmarshall = isUnmarshall;
        this.uml_triggers = uml_triggers;
    }

    public String getIsunmarshall() {
        return isUnmarshall;
    }

    public void setIsunmarshall(String isUnmarshall) {
        this.isUnmarshall = isUnmarshall;
    }

    public List<uml_Trigger> getUml_triggers() {
        return uml_triggers;
    }

    public void addUml_trigger(Uml_trigger uml_trigger) {
        this.uml_triggers.add(uml_trigger);
    }

}