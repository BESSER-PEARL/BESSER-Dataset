





import java.util.List;
import java.util.ArrayList;

public class tables_ForeignKey  {

    private String name;





    private tables_Table tables_table;




    private tables_Column tables_column;




    private tables_Column tables_column;


    public tables_ForeignKey(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tables_Table getTables_table() {
        return tables_table;
    }

    public void setTables_table(tables_Table tables_table) {
        this.tables_table = tables_table;
    }
    public tables_Column getTables_column() {
        return tables_column;
    }

    public void setTables_column(tables_Column tables_column) {
        this.tables_column = tables_column;
    }
    public tables_Column getTables_column() {
        return tables_column;
    }

    public void setTables_column(tables_Column tables_column) {
        this.tables_column = tables_column;
    }

}