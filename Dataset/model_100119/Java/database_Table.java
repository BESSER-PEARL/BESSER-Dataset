





import java.util.List;
import java.util.ArrayList;

public class database_Table extends RefTable {

    private String name;





    private List<database_RefPKey> database_refpkeys;




    private List<database_RefColumn> database_refcolumns;




    private List<database_RefFKey> database_reffkeys;


    public database_Table(
        String name    ) {
        super(
        );
        this.name = name;
        this.database_refpkeys = new ArrayList<>();
        this.database_refcolumns = new ArrayList<>();
        this.database_reffkeys = new ArrayList<>();
    }

    public database_Table(
        String name        ArrayList<database_RefPKey> database_refpkeys,        ArrayList<database_RefColumn> database_refcolumns,        ArrayList<database_RefFKey> database_reffkeys    ) {
        this.name = name;
        this.database_refpkeys = database_refpkeys;
        this.database_refcolumns = database_refcolumns;
        this.database_reffkeys = database_reffkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<database_RefPKey> getDatabase_refpkeys() {
        return database_refpkeys;
    }

    public void addDatabase_refpkey(Database_refpkey database_refpkey) {
        this.database_refpkeys.add(database_refpkey);
    }
    public List<database_RefColumn> getDatabase_refcolumns() {
        return database_refcolumns;
    }

    public void addDatabase_refcolumn(Database_refcolumn database_refcolumn) {
        this.database_refcolumns.add(database_refcolumn);
    }
    public List<database_RefFKey> getDatabase_reffkeys() {
        return database_reffkeys;
    }

    public void addDatabase_reffkey(Database_reffkey database_reffkey) {
        this.database_reffkeys.add(database_reffkey);
    }

}