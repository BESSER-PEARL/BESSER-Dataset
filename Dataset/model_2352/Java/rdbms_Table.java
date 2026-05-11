





import java.util.List;
import java.util.ArrayList;

public class rdbms_Table extends RModelElement {






    private rdbms_ForeignKey rdbms_foreignkey;




    private rdbms_Schema rdbms_schema;




    private List<rdbms_ForeignKey> rdbms_foreignkeys;




    private List<rdbms_Column> rdbms_columns;




    private rdbms_Column rdbms_column;




    private rdbms_Schema rdbms_schema;




    private List<rdbms_Key> rdbms_keys;




    private rdbms_Key rdbms_key;


    public rdbms_Table(
    ) {
        super(
        );
        this.rdbms_foreignkeys = new ArrayList<>();
        this.rdbms_columns = new ArrayList<>();
        this.rdbms_keys = new ArrayList<>();
    }

    public rdbms_Table(
        ArrayList<rdbms_ForeignKey> rdbms_foreignkeys,        ArrayList<rdbms_Column> rdbms_columns,        ArrayList<rdbms_Key> rdbms_keys    ) {
        this.rdbms_foreignkeys = rdbms_foreignkeys;
        this.rdbms_columns = rdbms_columns;
        this.rdbms_keys = rdbms_keys;
    }


    public rdbms_ForeignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(rdbms_ForeignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
    }
    public rdbms_Schema getRdbms_schema() {
        return rdbms_schema;
    }

    public void setRdbms_schema(rdbms_Schema rdbms_schema) {
        this.rdbms_schema = rdbms_schema;
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
    public rdbms_Column getRdbms_column() {
        return rdbms_column;
    }

    public void setRdbms_column(rdbms_Column rdbms_column) {
        this.rdbms_column = rdbms_column;
    }
    public rdbms_Schema getRdbms_schema() {
        return rdbms_schema;
    }

    public void setRdbms_schema(rdbms_Schema rdbms_schema) {
        this.rdbms_schema = rdbms_schema;
    }
    public List<rdbms_Key> getRdbms_keys() {
        return rdbms_keys;
    }

    public void addRdbms_key(Rdbms_key rdbms_key) {
        this.rdbms_keys.add(rdbms_key);
    }
    public rdbms_Key getRdbms_key() {
        return rdbms_key;
    }

    public void setRdbms_key(rdbms_Key rdbms_key) {
        this.rdbms_key = rdbms_key;
    }

}