





import java.util.List;
import java.util.ArrayList;

public class rdbms_ForeignKey  {






    private rdbms_Table rdbms_table;




    private List<rdbms_Column> rdbms_columns;




    private rdbms_RDBMSModel rdbms_rdbmsmodel;




    private rdbms_Table rdbms_table;


    public rdbms_ForeignKey(
    ) {
        this.rdbms_columns = new ArrayList<>();
    }

    public rdbms_ForeignKey(
        ArrayList<rdbms_Column> rdbms_columns    ) {
        this.rdbms_columns = rdbms_columns;
    }


    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public List<rdbms_Column> getRdbms_columns() {
        return rdbms_columns;
    }

    public void addRdbms_column(Rdbms_column rdbms_column) {
        this.rdbms_columns.add(rdbms_column);
    }
    public rdbms_RDBMSModel getRdbms_rdbmsmodel() {
        return rdbms_rdbmsmodel;
    }

    public void setRdbms_rdbmsmodel(rdbms_RDBMSModel rdbms_rdbmsmodel) {
        this.rdbms_rdbmsmodel = rdbms_rdbmsmodel;
    }
    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }

}