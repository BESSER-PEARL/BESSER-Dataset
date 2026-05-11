





import java.util.List;
import java.util.ArrayList;

public class database_Table extends AbstractTable {






    private List<database_Constraint> database_constraints;




    private List<database_Index> database_indexs;




    private database_Index database_index;




    private database_Constraint database_constraint;




    private database_PrimaryKey database_primarykey;




    private database_ForeignKey database_foreignkey;




    private database_PrimaryKey database_primarykey;




    private database_ForeignKey database_foreignkey;




    private List<database_ForeignKey> database_foreignkeys;


    public database_Table(
    ) {
        super(
        );
        this.database_constraints = new ArrayList<>();
        this.database_indexs = new ArrayList<>();
        this.database_foreignkeys = new ArrayList<>();
    }

    public database_Table(
        ArrayList<database_Constraint> database_constraints,        ArrayList<database_Index> database_indexs,        ArrayList<database_ForeignKey> database_foreignkeys    ) {
        this.database_constraints = database_constraints;
        this.database_indexs = database_indexs;
        this.database_foreignkeys = database_foreignkeys;
    }


    public List<database_Constraint> getDatabase_constraints() {
        return database_constraints;
    }

    public void addDatabase_constraint(Database_constraint database_constraint) {
        this.database_constraints.add(database_constraint);
    }
    public List<database_Index> getDatabase_indexs() {
        return database_indexs;
    }

    public void addDatabase_index(Database_index database_index) {
        this.database_indexs.add(database_index);
    }
    public database_Index getDatabase_index() {
        return database_index;
    }

    public void setDatabase_index(database_Index database_index) {
        this.database_index = database_index;
    }
    public database_Constraint getDatabase_constraint() {
        return database_constraint;
    }

    public void setDatabase_constraint(database_Constraint database_constraint) {
        this.database_constraint = database_constraint;
    }
    public database_PrimaryKey getDatabase_primarykey() {
        return database_primarykey;
    }

    public void setDatabase_primarykey(database_PrimaryKey database_primarykey) {
        this.database_primarykey = database_primarykey;
    }
    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }
    public database_PrimaryKey getDatabase_primarykey() {
        return database_primarykey;
    }

    public void setDatabase_primarykey(database_PrimaryKey database_primarykey) {
        this.database_primarykey = database_primarykey;
    }
    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }
    public List<database_ForeignKey> getDatabase_foreignkeys() {
        return database_foreignkeys;
    }

    public void addDatabase_foreignkey(Database_foreignkey database_foreignkey) {
        this.database_foreignkeys.add(database_foreignkey);
    }

}