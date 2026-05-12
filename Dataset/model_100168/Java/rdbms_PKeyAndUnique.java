





import java.util.List;
import java.util.ArrayList;

public class rdbms_PKeyAndUnique extends Constraints {






    private rdbms_ForeignKey rdbms_foreignkey;




    private List<rdbms_Column> rdbms_columns;




    private rdbms_Column rdbms_column;


    public rdbms_PKeyAndUnique(
    ) {
        super(
        );
        this.rdbms_columns = new ArrayList<>();
    }

    public rdbms_PKeyAndUnique(
        ArrayList<rdbms_Column> rdbms_columns    ) {
        this.rdbms_columns = rdbms_columns;
    }


    public rdbms_ForeignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(rdbms_ForeignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
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

}