





import java.util.List;
import java.util.ArrayList;

public class sqls_TriggerUpdate extends TriggerAction {






    private List<sqls_Column> sqls_columns;


    public sqls_TriggerUpdate(
    ) {
        super(
        );
        this.sqls_columns = new ArrayList<>();
    }

    public sqls_TriggerUpdate(
        ArrayList<sqls_Column> sqls_columns    ) {
        this.sqls_columns = sqls_columns;
    }


    public List<sqls_Column> getSqls_columns() {
        return sqls_columns;
    }

    public void addSqls_column(Sqls_column sqls_column) {
        this.sqls_columns.add(sqls_column);
    }

}