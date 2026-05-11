





import java.util.List;
import java.util.ArrayList;

public class Relational_Database extends Named {






    private List<Relational_Table> relational_tables;




    private List<Relational_Type> relational_types;


    public Relational_Database(
    ) {
        super(
        );
        this.relational_tables = new ArrayList<>();
        this.relational_types = new ArrayList<>();
    }

    public Relational_Database(
        ArrayList<Relational_Table> relational_tables,        ArrayList<Relational_Type> relational_types    ) {
        this.relational_tables = relational_tables;
        this.relational_types = relational_types;
    }


    public List<Relational_Table> getRelational_tables() {
        return relational_tables;
    }

    public void addRelational_table(Relational_table relational_table) {
        this.relational_tables.add(relational_table);
    }
    public List<Relational_Type> getRelational_types() {
        return relational_types;
    }

    public void addRelational_type(Relational_type relational_type) {
        this.relational_types.add(relational_type);
    }

}