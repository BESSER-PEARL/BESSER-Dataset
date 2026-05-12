





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_CreateTable extends Operation {

    private String tableName;





    private List<TableConstraint> tableconstraints;




    private PrimaryKey primarykey;




    private List<TableColumn> tablecolumns;




    private Sequence sequence;


    public mm_rdb_CreateTable(
        String tableName    ) {
        super(
        );
        this.tableName = tableName;
        this.tableconstraints = new ArrayList<>();
        this.tablecolumns = new ArrayList<>();
    }

    public mm_rdb_CreateTable(
        String tableName        ArrayList<TableConstraint> tableconstraints,        ArrayList<TableColumn> tablecolumns    ) {
        this.tableName = tableName;
        this.tableconstraints = tableconstraints;
        this.tablecolumns = tablecolumns;
    }

    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }

    public List<TableConstraint> getTableconstraints() {
        return tableconstraints;
    }

    public void addTableconstraint(Tableconstraint tableconstraint) {
        this.tableconstraints.add(tableconstraint);
    }
    public PrimaryKey getPrimarykey() {
        return primarykey;
    }

    public void setPrimarykey(PrimaryKey primarykey) {
        this.primarykey = primarykey;
    }
    public List<TableColumn> getTablecolumns() {
        return tablecolumns;
    }

    public void addTablecolumn(Tablecolumn tablecolumn) {
        this.tablecolumns.add(tablecolumn);
    }
    public Sequence getSequence() {
        return sequence;
    }

    public void setSequence(Sequence sequence) {
        this.sequence = sequence;
    }

}