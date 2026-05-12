





import java.util.List;
import java.util.ArrayList;

public class sqls_UniqueTableConstraint extends TableConstraint {

    private String name;





    private List<sqls_Column> sqls_columns;


    public sqls_UniqueTableConstraint(
        String name    ) {
        super(
        );
        this.name = name;
        this.sqls_columns = new ArrayList<>();
    }

    public sqls_UniqueTableConstraint(
        String name        ArrayList<sqls_Column> sqls_columns    ) {
        this.name = name;
        this.sqls_columns = sqls_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sqls_Column> getSqls_columns() {
        return sqls_columns;
    }

    public void addSqls_column(Sqls_column sqls_column) {
        this.sqls_columns.add(sqls_column);
    }

}