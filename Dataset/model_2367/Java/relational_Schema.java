





import java.util.List;
import java.util.ArrayList;

public class relational_Schema extends ModelElement {

    private String name;





    private relational_Database relational_database;




    private relational_Database relational_database;




    private List<relational_Table> relational_tables;




    private relational_Table relational_table;


    public relational_Schema(
        String name    ) {
        super(
        );
        this.name = name;
        this.relational_tables = new ArrayList<>();
    }

    public relational_Schema(
        String name        ArrayList<relational_Table> relational_tables    ) {
        this.name = name;
        this.relational_tables = relational_tables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public relational_Database getRelational_database() {
        return relational_database;
    }

    public void setRelational_database(relational_Database relational_database) {
        this.relational_database = relational_database;
    }
    public relational_Database getRelational_database() {
        return relational_database;
    }

    public void setRelational_database(relational_Database relational_database) {
        this.relational_database = relational_database;
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