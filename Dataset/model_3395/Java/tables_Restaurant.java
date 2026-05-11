





import java.util.List;
import java.util.ArrayList;

public class tables_Restaurant  {






    private List<tables_Table> tables_tables;




    private List<tables_Waitress> tables_waitresss;


    public tables_Restaurant(
    ) {
        this.tables_tables = new ArrayList<>();
        this.tables_waitresss = new ArrayList<>();
    }

    public tables_Restaurant(
        ArrayList<tables_Table> tables_tables,        ArrayList<tables_Waitress> tables_waitresss    ) {
        this.tables_tables = tables_tables;
        this.tables_waitresss = tables_waitresss;
    }


    public List<tables_Table> getTables_tables() {
        return tables_tables;
    }

    public void addTables_table(Tables_table tables_table) {
        this.tables_tables.add(tables_table);
    }
    public List<tables_Waitress> getTables_waitresss() {
        return tables_waitresss;
    }

    public void addTables_waitress(Tables_waitress tables_waitress) {
        this.tables_waitresss.add(tables_waitress);
    }

}