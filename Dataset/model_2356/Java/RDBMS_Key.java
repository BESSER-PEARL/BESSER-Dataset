





import java.util.List;
import java.util.ArrayList;

public class RDBMS_Key  {

    private String name;





    private List<RDBMS_Column> rdbms_columns;




    private List<RDBMS_ForeignKey> rdbms_foreignkeys;




    private RDBMS_Table rdbms_table;




    private RDBMS_Table rdbms_table;




    private RDBMS_ForeignKey rdbms_foreignkey;




    private RDBMS_Column rdbms_column;


    public RDBMS_Key(
        String name    ) {
        this.name = name;
        this.rdbms_columns = new ArrayList<>();
        this.rdbms_foreignkeys = new ArrayList<>();
    }

    public RDBMS_Key(
        String name        ArrayList<RDBMS_Column> rdbms_columns,        ArrayList<RDBMS_ForeignKey> rdbms_foreignkeys    ) {
        this.name = name;
        this.rdbms_columns = rdbms_columns;
        this.rdbms_foreignkeys = rdbms_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<RDBMS_Column> getRdbms_columns() {
        return rdbms_columns;
    }

    public void addRdbms_column(Rdbms_column rdbms_column) {
        this.rdbms_columns.add(rdbms_column);
    }
    public List<RDBMS_ForeignKey> getRdbms_foreignkeys() {
        return rdbms_foreignkeys;
    }

    public void addRdbms_foreignkey(Rdbms_foreignkey rdbms_foreignkey) {
        this.rdbms_foreignkeys.add(rdbms_foreignkey);
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
    public RDBMS_ForeignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(RDBMS_ForeignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
    }
    public RDBMS_Column getRdbms_column() {
        return rdbms_column;
    }

    public void setRdbms_column(RDBMS_Column rdbms_column) {
        this.rdbms_column = rdbms_column;
    }

}