





import java.util.List;
import java.util.ArrayList;

public class relational_Schema extends SQLObject {






    private relational_Trigger relational_trigger;




    private List<relational_Trigger> relational_triggers;


    public relational_Schema(
    ) {
        super(
        );
        this.relational_triggers = new ArrayList<>();
    }

    public relational_Schema(
        ArrayList<relational_Trigger> relational_triggers    ) {
        this.relational_triggers = relational_triggers;
    }


    public relational_Trigger getRelational_trigger() {
        return relational_trigger;
    }

    public void setRelational_trigger(relational_Trigger relational_trigger) {
        this.relational_trigger = relational_trigger;
    }
    public List<relational_Trigger> getRelational_triggers() {
        return relational_triggers;
    }

    public void addRelational_trigger(Relational_trigger relational_trigger) {
        this.relational_triggers.add(relational_trigger);
    }

}