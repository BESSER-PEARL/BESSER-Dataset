





import java.util.List;
import java.util.ArrayList;

public class rdb_Table extends NamedColumnSet {






    private List<ForeignKey> foreignkeys;




    private List<Index> indexs;




    private List<CheckConstraint> checkconstraints;




    private List<rdb_TableColumn> rdb_tablecolumns;


    public rdb_Table(
    ) {
        super(
        );
        this.foreignkeys = new ArrayList<>();
        this.indexs = new ArrayList<>();
        this.checkconstraints = new ArrayList<>();
        this.rdb_tablecolumns = new ArrayList<>();
    }

    public rdb_Table(
        ArrayList<ForeignKey> foreignkeys,        ArrayList<Index> indexs,        ArrayList<CheckConstraint> checkconstraints,        ArrayList<rdb_TableColumn> rdb_tablecolumns    ) {
        this.foreignkeys = foreignkeys;
        this.indexs = indexs;
        this.checkconstraints = checkconstraints;
        this.rdb_tablecolumns = rdb_tablecolumns;
    }


    public List<ForeignKey> getForeignkeys() {
        return foreignkeys;
    }

    public void addForeignkey(Foreignkey foreignkey) {
        this.foreignkeys.add(foreignkey);
    }
    public List<Index> getIndexs() {
        return indexs;
    }

    public void addIndex(Index index) {
        this.indexs.add(index);
    }
    public List<CheckConstraint> getCheckconstraints() {
        return checkconstraints;
    }

    public void addCheckconstraint(Checkconstraint checkconstraint) {
        this.checkconstraints.add(checkconstraint);
    }
    public List<rdb_TableColumn> getRdb_tablecolumns() {
        return rdb_tablecolumns;
    }

    public void addRdb_tablecolumn(Rdb_tablecolumn rdb_tablecolumn) {
        this.rdb_tablecolumns.add(rdb_tablecolumn);
    }

}