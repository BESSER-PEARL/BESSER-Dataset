





import java.util.List;
import java.util.ArrayList;

public class RDBMSMM_RDBMSModel  {






    private List<RDBMSMM_Table> rdbmsmm_tables;


    public RDBMSMM_RDBMSModel(
    ) {
        this.rdbmsmm_tables = new ArrayList<>();
    }

    public RDBMSMM_RDBMSModel(
        ArrayList<RDBMSMM_Table> rdbmsmm_tables    ) {
        this.rdbmsmm_tables = rdbmsmm_tables;
    }


    public List<RDBMSMM_Table> getRdbmsmm_tables() {
        return rdbmsmm_tables;
    }

    public void addRdbmsmm_table(Rdbmsmm_table rdbmsmm_table) {
        this.rdbmsmm_tables.add(rdbmsmm_table);
    }

}