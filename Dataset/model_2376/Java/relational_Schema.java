





import java.util.List;
import java.util.ArrayList;

public class relational_Schema extends SQLObject {






    private relational_Trigger relational_trigger;




    private List<relational_Table> relational_tables;




    private List<relational_Trigger> relational_triggers;




    private relational_Table relational_table;


    public relational_Schema(
    ) {
        super(
        );
        this.relational_tables = new ArrayList<>();
        this.relational_triggers = new ArrayList<>();
    }

    public relational_Schema(
        ArrayList<relational_Table> relational_tables,        ArrayList<relational_Trigger> relational_triggers    ) {
        this.relational_tables = relational_tables;
        this.relational_triggers = relational_triggers;
    }


    public relational_Trigger getRelational_trigger() {
        return relational_trigger;
    }

    public void setRelational_trigger(relational_Trigger relational_trigger) {
        this.relational_trigger = relational_trigger;
    }
    public List<relational_Table> getRelational_tables() {
        return relational_tables;
    }

    public void addRelational_table(Relational_table relational_table) {
        this.relational_tables.add(relational_table);
    }
    public List<relational_Trigger> getRelational_triggers() {
        return relational_triggers;
    }

    public void addRelational_trigger(Relational_trigger relational_trigger) {
        this.relational_triggers.add(relational_trigger);
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}