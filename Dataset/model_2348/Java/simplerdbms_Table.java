





import java.util.List;
import java.util.ArrayList;

public class simplerdbms_Table extends RModelElement {






    private simplerdbms_Column simplerdbms_column;




    private simplerdbms_Schema simplerdbms_schema;




    private simplerdbms_Schema simplerdbms_schema;




    private List<simplerdbms_Key> simplerdbms_keys;




    private simplerdbms_Key simplerdbms_key;




    private simplerdbms_ForeignKey simplerdbms_foreignkey;




    private List<simplerdbms_Column> simplerdbms_columns;




    private List<simplerdbms_ForeignKey> simplerdbms_foreignkeys;


    public simplerdbms_Table(
    ) {
        super(
        );
        this.simplerdbms_keys = new ArrayList<>();
        this.simplerdbms_columns = new ArrayList<>();
        this.simplerdbms_foreignkeys = new ArrayList<>();
    }

    public simplerdbms_Table(
        ArrayList<simplerdbms_Key> simplerdbms_keys,        ArrayList<simplerdbms_Column> simplerdbms_columns,        ArrayList<simplerdbms_ForeignKey> simplerdbms_foreignkeys    ) {
        this.simplerdbms_keys = simplerdbms_keys;
        this.simplerdbms_columns = simplerdbms_columns;
        this.simplerdbms_foreignkeys = simplerdbms_foreignkeys;
    }


    public simplerdbms_Column getSimplerdbms_column() {
        return simplerdbms_column;
    }

    public void setSimplerdbms_column(simplerdbms_Column simplerdbms_column) {
        this.simplerdbms_column = simplerdbms_column;
    }
    public simplerdbms_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simplerdbms_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }
    public simplerdbms_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(simplerdbms_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }
    public List<simplerdbms_Key> getSimplerdbms_keys() {
        return simplerdbms_keys;
    }

    public void addSimplerdbms_key(Simplerdbms_key simplerdbms_key) {
        this.simplerdbms_keys.add(simplerdbms_key);
    }
    public simplerdbms_Key getSimplerdbms_key() {
        return simplerdbms_key;
    }

    public void setSimplerdbms_key(simplerdbms_Key simplerdbms_key) {
        this.simplerdbms_key = simplerdbms_key;
    }
    public simplerdbms_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(simplerdbms_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }
    public List<simplerdbms_Column> getSimplerdbms_columns() {
        return simplerdbms_columns;
    }

    public void addSimplerdbms_column(Simplerdbms_column simplerdbms_column) {
        this.simplerdbms_columns.add(simplerdbms_column);
    }
    public List<simplerdbms_ForeignKey> getSimplerdbms_foreignkeys() {
        return simplerdbms_foreignkeys;
    }

    public void addSimplerdbms_foreignkey(Simplerdbms_foreignkey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkeys.add(simplerdbms_foreignkey);
    }

}