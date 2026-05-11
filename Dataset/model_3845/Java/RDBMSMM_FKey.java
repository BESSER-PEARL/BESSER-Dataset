





import java.util.List;
import java.util.ArrayList;

public class RDBMSMM_FKey  {






    private RDBMSMM_Table rdbmsmm_table;




    private RDBMSMM_Table rdbmsmm_table;




    private List<RDBMSMM_Column> rdbmsmm_columns;


    public RDBMSMM_FKey(
    ) {
        this.rdbmsmm_columns = new ArrayList<>();
    }

    public RDBMSMM_FKey(
        ArrayList<RDBMSMM_Column> rdbmsmm_columns    ) {
        this.rdbmsmm_columns = rdbmsmm_columns;
    }


    public RDBMSMM_Table getRdbmsmm_table() {
        return rdbmsmm_table;
    }

    public void setRdbmsmm_table(RDBMSMM_Table rdbmsmm_table) {
        this.rdbmsmm_table = rdbmsmm_table;
    }
    public RDBMSMM_Table getRdbmsmm_table() {
        return rdbmsmm_table;
    }

    public void setRdbmsmm_table(RDBMSMM_Table rdbmsmm_table) {
        this.rdbmsmm_table = rdbmsmm_table;
    }
    public List<RDBMSMM_Column> getRdbmsmm_columns() {
        return rdbmsmm_columns;
    }

    public void addRdbmsmm_column(Rdbmsmm_column rdbmsmm_column) {
        this.rdbmsmm_columns.add(rdbmsmm_column);
    }

}