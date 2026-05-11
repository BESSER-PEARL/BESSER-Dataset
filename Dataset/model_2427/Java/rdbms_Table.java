





import java.util.List;
import java.util.ArrayList;

public class rdbms_Table extends ModelElement {






    private List<rdbms_UniqueCon> rdbms_uniquecons;




    private rdbms_ForeignKey rdbms_foreignkey;




    private List<rdbms_ForeignKey> rdbms_foreignkeys;




    private List<rdbms_Column> rdbms_columns;




    private List<rdbms_CheckCon> rdbms_checkcons;




    private rdbms_ForeignKey rdbms_foreignkey;




    private rdbms_Database rdbms_database;




    private rdbms_PrimaryKeyCon rdbms_primarykeycon;


    public rdbms_Table(
    ) {
        super(
        );
        this.rdbms_uniquecons = new ArrayList<>();
        this.rdbms_foreignkeys = new ArrayList<>();
        this.rdbms_columns = new ArrayList<>();
        this.rdbms_checkcons = new ArrayList<>();
    }

    public rdbms_Table(
        ArrayList<rdbms_UniqueCon> rdbms_uniquecons,        ArrayList<rdbms_ForeignKey> rdbms_foreignkeys,        ArrayList<rdbms_Column> rdbms_columns,        ArrayList<rdbms_CheckCon> rdbms_checkcons    ) {
        this.rdbms_uniquecons = rdbms_uniquecons;
        this.rdbms_foreignkeys = rdbms_foreignkeys;
        this.rdbms_columns = rdbms_columns;
        this.rdbms_checkcons = rdbms_checkcons;
    }


    public List<rdbms_UniqueCon> getRdbms_uniquecons() {
        return rdbms_uniquecons;
    }

    public void addRdbms_uniquecon(Rdbms_uniquecon rdbms_uniquecon) {
        this.rdbms_uniquecons.add(rdbms_uniquecon);
    }
    public rdbms_ForeignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(rdbms_ForeignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
    }
    public List<rdbms_ForeignKey> getRdbms_foreignkeys() {
        return rdbms_foreignkeys;
    }

    public void addRdbms_foreignkey(Rdbms_foreignkey rdbms_foreignkey) {
        this.rdbms_foreignkeys.add(rdbms_foreignkey);
    }
    public List<rdbms_Column> getRdbms_columns() {
        return rdbms_columns;
    }

    public void addRdbms_column(Rdbms_column rdbms_column) {
        this.rdbms_columns.add(rdbms_column);
    }
    public List<rdbms_CheckCon> getRdbms_checkcons() {
        return rdbms_checkcons;
    }

    public void addRdbms_checkcon(Rdbms_checkcon rdbms_checkcon) {
        this.rdbms_checkcons.add(rdbms_checkcon);
    }
    public rdbms_ForeignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(rdbms_ForeignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
    }
    public rdbms_Database getRdbms_database() {
        return rdbms_database;
    }

    public void setRdbms_database(rdbms_Database rdbms_database) {
        this.rdbms_database = rdbms_database;
    }
    public rdbms_PrimaryKeyCon getRdbms_primarykeycon() {
        return rdbms_primarykeycon;
    }

    public void setRdbms_primarykeycon(rdbms_PrimaryKeyCon rdbms_primarykeycon) {
        this.rdbms_primarykeycon = rdbms_primarykeycon;
    }

}