





import java.util.List;
import java.util.ArrayList;

public class rdbms_ForeignKey extends RModelElement {






    private List<rdbms_Column> rdbms_columns;




    private rdbms_Key rdbms_key;




    private rdbms_Column rdbms_column;


    public rdbms_ForeignKey(
    ) {
        super(
        );
        this.rdbms_columns = new ArrayList<>();
    }

    public rdbms_ForeignKey(
        ArrayList<rdbms_Column> rdbms_columns    ) {
        this.rdbms_columns = rdbms_columns;
    }


    public List<rdbms_Column> getRdbms_columns() {
        return rdbms_columns;
    }

    public void addRdbms_column(Rdbms_column rdbms_column) {
        this.rdbms_columns.add(rdbms_column);
    }
    public rdbms_Key getRdbms_key() {
        return rdbms_key;
    }

    public void setRdbms_key(rdbms_Key rdbms_key) {
        this.rdbms_key = rdbms_key;
    }
    public rdbms_Column getRdbms_column() {
        return rdbms_column;
    }

    public void setRdbms_column(rdbms_Column rdbms_column) {
        this.rdbms_column = rdbms_column;
    }

}