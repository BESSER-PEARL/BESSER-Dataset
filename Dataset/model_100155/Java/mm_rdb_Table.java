





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_Table extends rdb_DbObject, rdb_Relation {






    private Schema schema;




    private List<TableConstraint> tableconstraints;


    public mm_rdb_Table(
    ) {
        super(
        );
        this.tableconstraints = new ArrayList<>();
    }

    public mm_rdb_Table(
        ArrayList<TableConstraint> tableconstraints    ) {
        this.tableconstraints = tableconstraints;
    }


    public Schema getSchema() {
        return schema;
    }

    public void setSchema(Schema schema) {
        this.schema = schema;
    }
    public List<TableConstraint> getTableconstraints() {
        return tableconstraints;
    }

    public void addTableconstraint(Tableconstraint tableconstraint) {
        this.tableconstraints.add(tableconstraint);
    }

}