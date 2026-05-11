





import java.util.List;
import java.util.ArrayList;

public class Relational_Column extends Named {






    private Relational_Table relational_table;




    private Relational_Table relational_table;




    private List<Relational_Table> relational_tables;




    private Relational_Table relational_table;


    public Relational_Column(
    ) {
        super(
        );
        this.relational_tables = new ArrayList<>();
    }

    public Relational_Column(
        ArrayList<Relational_Table> relational_tables    ) {
        this.relational_tables = relational_tables;
    }


    public Relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(Relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public Relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(Relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public List<Relational_Table> getRelational_tables() {
        return relational_tables;
    }

    public void addRelational_table(Relational_table relational_table) {
        this.relational_tables.add(relational_table);
    }
    public Relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(Relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}