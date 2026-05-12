





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_AddColumn extends Operation {

    private String newColumnName;





    private List<ColumnConstraint> columnconstraints;




    private Table table;


    public mm_rdb_AddColumn(
        String newColumnName    ) {
        super(
        );
        this.newColumnName = newColumnName;
        this.columnconstraints = new ArrayList<>();
    }

    public mm_rdb_AddColumn(
        String newColumnName        ArrayList<ColumnConstraint> columnconstraints    ) {
        this.newColumnName = newColumnName;
        this.columnconstraints = columnconstraints;
    }

    public String getNewcolumnname() {
        return newColumnName;
    }

    public void setNewcolumnname(String newColumnName) {
        this.newColumnName = newColumnName;
    }

    public List<ColumnConstraint> getColumnconstraints() {
        return columnconstraints;
    }

    public void addColumnconstraint(Columnconstraint columnconstraint) {
        this.columnconstraints.add(columnconstraint);
    }
    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}