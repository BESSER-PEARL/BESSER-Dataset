





import java.util.List;
import java.util.ArrayList;

public class simplerdbms_Table extends RModelElement {






    private simplerdbms_Column simplerdbms_column;




    private List<simplerdbms_Key> simplerdbms_keys;




    private simplerdbms_Key simplerdbms_key;




    private List<simplerdbms_Column> simplerdbms_columns;


    public simplerdbms_Table(
    ) {
        super(
        );
        this.simplerdbms_keys = new ArrayList<>();
        this.simplerdbms_columns = new ArrayList<>();
    }

    public simplerdbms_Table(
        ArrayList<simplerdbms_Key> simplerdbms_keys,        ArrayList<simplerdbms_Column> simplerdbms_columns    ) {
        this.simplerdbms_keys = simplerdbms_keys;
        this.simplerdbms_columns = simplerdbms_columns;
    }


    public simplerdbms_Column getSimplerdbms_column() {
        return simplerdbms_column;
    }

    public void setSimplerdbms_column(simplerdbms_Column simplerdbms_column) {
        this.simplerdbms_column = simplerdbms_column;
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
    public List<simplerdbms_Column> getSimplerdbms_columns() {
        return simplerdbms_columns;
    }

    public void addSimplerdbms_column(Simplerdbms_column simplerdbms_column) {
        this.simplerdbms_columns.add(simplerdbms_column);
    }

}