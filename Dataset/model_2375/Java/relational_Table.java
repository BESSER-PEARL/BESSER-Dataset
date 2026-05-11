





import java.util.List;
import java.util.ArrayList;

public class relational_Table extends SQLObject {






    private relational_Trigger relational_trigger;




    private relational_Schema relational_schema;




    private List<relational_Trigger> relational_triggers;




    private relational_Trigger relational_trigger;




    private relational_Schema relational_schema;




    private List<relational_Trigger> relational_triggers;


    public relational_Table(
    ) {
        super(
        );
        this.relational_triggers = new ArrayList<>();
        this.relational_triggers = new ArrayList<>();
    }

    public relational_Table(
        ArrayList<relational_Trigger> relational_triggers,        ArrayList<relational_Trigger> relational_triggers    ) {
        this.relational_triggers = relational_triggers;
        this.relational_triggers = relational_triggers;
    }


    public relational_Trigger getRelational_trigger() {
        return relational_trigger;
    }

    public void setRelational_trigger(relational_Trigger relational_trigger) {
        this.relational_trigger = relational_trigger;
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public List<relational_Trigger> getRelational_triggers() {
        return relational_triggers;
    }

    public void addRelational_trigger(Relational_trigger relational_trigger) {
        this.relational_triggers.add(relational_trigger);
    }
    public relational_Trigger getRelational_trigger() {
        return relational_trigger;
    }

    public void setRelational_trigger(relational_Trigger relational_trigger) {
        this.relational_trigger = relational_trigger;
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public List<relational_Trigger> getRelational_triggers() {
        return relational_triggers;
    }

    public void addRelational_trigger(Relational_trigger relational_trigger) {
        this.relational_triggers.add(relational_trigger);
    }

}