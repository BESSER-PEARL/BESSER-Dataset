





import java.util.List;
import java.util.ArrayList;

public class SmartHome_Home extends NamedElement {

    private float startDay;
    private float speed;





    private List<SmartHome_Rule> smarthome_rules;


    public SmartHome_Home(
        float startDay,        float speed    ) {
        super(
        );
        this.startDay = startDay;
        this.speed = speed;
        this.smarthome_rules = new ArrayList<>();
    }

    public SmartHome_Home(
        float startDay,        float speed        ArrayList<SmartHome_Rule> smarthome_rules    ) {
        this.startDay = startDay;
        this.speed = speed;
        this.smarthome_rules = smarthome_rules;
    }

    public float getStartday() {
        return startDay;
    }

    public void setStartday(float startDay) {
        this.startDay = startDay;
    }
    public float getSpeed() {
        return speed;
    }

    public void setSpeed(float speed) {
        this.speed = speed;
    }

    public List<SmartHome_Rule> getSmarthome_rules() {
        return smarthome_rules;
    }

    public void addSmarthome_rule(Smarthome_rule smarthome_rule) {
        this.smarthome_rules.add(smarthome_rule);
    }

}