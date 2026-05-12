





import java.util.List;
import java.util.ArrayList;

public class relational_Schema extends RelationalEntity {






    private List<relational_Table> relational_tables;




    private relational_Table relational_table;


    public relational_Schema(
    ) {
        super(
        );
        this.relational_tables = new ArrayList<>();
    }

    public relational_Schema(
        ArrayList<relational_Table> relational_tables    ) {
        this.relational_tables = relational_tables;
    }


    public List<relational_Table> getRelational_tables() {
        return relational_tables;
    }

    public void addRelational_table(Relational_table relational_table) {
        this.relational_tables.add(relational_table);
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}