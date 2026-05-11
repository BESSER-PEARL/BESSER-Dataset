





import java.util.List;
import java.util.ArrayList;

public class tables_Chair  {

    private int order;





    private tables_Table tables_table;


    public tables_Chair(
        int order    ) {
        this.order = order;
    }


    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }

    public tables_Table getTables_table() {
        return tables_table;
    }

    public void setTables_table(tables_Table tables_table) {
        this.tables_table = tables_table;
    }

}