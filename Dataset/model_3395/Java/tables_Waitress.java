





import java.util.List;
import java.util.ArrayList;

public class tables_Waitress  {

    private String name;





    private List<tables_Table> tables_tables;


    public tables_Waitress(
        String name    ) {
        this.name = name;
        this.tables_tables = new ArrayList<>();
    }

    public tables_Waitress(
        String name        ArrayList<tables_Table> tables_tables    ) {
        this.name = name;
        this.tables_tables = tables_tables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tables_Table> getTables_tables() {
        return tables_tables;
    }

    public void addTables_table(Tables_table tables_table) {
        this.tables_tables.add(tables_table);
    }

}