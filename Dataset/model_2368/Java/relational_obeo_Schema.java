





import java.util.List;
import java.util.ArrayList;

public class relational_obeo_Schema extends ModelElement {

    private String name;





    private relational_obeo_Database relational_obeo_database;




    private relational_obeo_Database relational_obeo_database;




    private relational_obeo_Table relational_obeo_table;




    private List<relational_obeo_Table> relational_obeo_tables;


    public relational_obeo_Schema(
        String name    ) {
        super(
        );
        this.name = name;
        this.relational_obeo_tables = new ArrayList<>();
    }

    public relational_obeo_Schema(
        String name        ArrayList<relational_obeo_Table> relational_obeo_tables    ) {
        this.name = name;
        this.relational_obeo_tables = relational_obeo_tables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public relational_obeo_Database getRelational_obeo_database() {
        return relational_obeo_database;
    }

    public void setRelational_obeo_database(relational_obeo_Database relational_obeo_database) {
        this.relational_obeo_database = relational_obeo_database;
    }
    public relational_obeo_Database getRelational_obeo_database() {
        return relational_obeo_database;
    }

    public void setRelational_obeo_database(relational_obeo_Database relational_obeo_database) {
        this.relational_obeo_database = relational_obeo_database;
    }
    public relational_obeo_Table getRelational_obeo_table() {
        return relational_obeo_table;
    }

    public void setRelational_obeo_table(relational_obeo_Table relational_obeo_table) {
        this.relational_obeo_table = relational_obeo_table;
    }
    public List<relational_obeo_Table> getRelational_obeo_tables() {
        return relational_obeo_tables;
    }

    public void addRelational_obeo_table(Relational_obeo_table relational_obeo_table) {
        this.relational_obeo_tables.add(relational_obeo_table);
    }

}