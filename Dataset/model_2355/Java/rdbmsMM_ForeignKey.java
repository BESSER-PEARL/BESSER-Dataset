





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_ForeignKey extends RModelElement {






    private rdbmsMM_Column rdbmsmm_column;




    private rdbmsMM_Key rdbmsmm_key;




    private rdbmsMM_Key rdbmsmm_key;




    private List<rdbmsMM_Column> rdbmsmm_columns;


    public rdbmsMM_ForeignKey(
    ) {
        super(
        );
        this.rdbmsmm_columns = new ArrayList<>();
    }

    public rdbmsMM_ForeignKey(
        ArrayList<rdbmsMM_Column> rdbmsmm_columns    ) {
        this.rdbmsmm_columns = rdbmsmm_columns;
    }


    public rdbmsMM_Column getRdbmsmm_column() {
        return rdbmsmm_column;
    }

    public void setRdbmsmm_column(rdbmsMM_Column rdbmsmm_column) {
        this.rdbmsmm_column = rdbmsmm_column;
    }
    public rdbmsMM_Key getRdbmsmm_key() {
        return rdbmsmm_key;
    }

    public void setRdbmsmm_key(rdbmsMM_Key rdbmsmm_key) {
        this.rdbmsmm_key = rdbmsmm_key;
    }
    public rdbmsMM_Key getRdbmsmm_key() {
        return rdbmsmm_key;
    }

    public void setRdbmsmm_key(rdbmsMM_Key rdbmsmm_key) {
        this.rdbmsmm_key = rdbmsmm_key;
    }
    public List<rdbmsMM_Column> getRdbmsmm_columns() {
        return rdbmsmm_columns;
    }

    public void addRdbmsmm_column(Rdbmsmm_column rdbmsmm_column) {
        this.rdbmsmm_columns.add(rdbmsmm_column);
    }

}