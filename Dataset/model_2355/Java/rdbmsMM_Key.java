





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_Key extends RModelElement {






    private rdbmsMM_Column rdbmsmm_column;




    private List<rdbmsMM_Column> rdbmsmm_columns;


    public rdbmsMM_Key(
    ) {
        super(
        );
        this.rdbmsmm_columns = new ArrayList<>();
    }

    public rdbmsMM_Key(
        ArrayList<rdbmsMM_Column> rdbmsmm_columns    ) {
        this.rdbmsmm_columns = rdbmsmm_columns;
    }


    public rdbmsMM_Column getRdbmsmm_column() {
        return rdbmsmm_column;
    }

    public void setRdbmsmm_column(rdbmsMM_Column rdbmsmm_column) {
        this.rdbmsmm_column = rdbmsmm_column;
    }
    public List<rdbmsMM_Column> getRdbmsmm_columns() {
        return rdbmsmm_columns;
    }

    public void addRdbmsmm_column(Rdbmsmm_column rdbmsmm_column) {
        this.rdbmsmm_columns.add(rdbmsmm_column);
    }

}