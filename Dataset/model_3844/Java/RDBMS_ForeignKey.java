





import java.util.List;
import java.util.ArrayList;

public class RDBMS_ForeignKey  {






    private RDBMS_Table rdbms_table;




    private RDBMS_Table rdbms_table;




    private List<RDBMS_Column> rdbms_columns;


    public RDBMS_ForeignKey(
    ) {
        this.rdbms_columns = new ArrayList<>();
    }

    public RDBMS_ForeignKey(
        ArrayList<RDBMS_Column> rdbms_columns    ) {
        this.rdbms_columns = rdbms_columns;
    }


    public RDBMS_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(RDBMS_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public RDBMS_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(RDBMS_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public List<RDBMS_Column> getRdbms_columns() {
        return rdbms_columns;
    }

    public void addRdbms_column(Rdbms_column rdbms_column) {
        this.rdbms_columns.add(rdbms_column);
    }

}