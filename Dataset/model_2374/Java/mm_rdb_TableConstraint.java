





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_TableConstraint extends rdb_Constraint, rdb_NamedElement {






    private Table table;


    public mm_rdb_TableConstraint(
    ) {
        super(
        );
    }



    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}