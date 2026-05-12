





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_Key  {

    private String name;





    private List<rdbmsMM_Column> rdbmsmm_columns;




    private List<rdbmsMM_ForeignKey> rdbmsmm_foreignkeys;




    private rdbmsMM_ForeignKey rdbmsmm_foreignkey;




    private rdbmsMM_Column rdbmsmm_column;




    private rdbmsMM_Table rdbmsmm_table;




    private rdbmsMM_Table rdbmsmm_table;


    public rdbmsMM_Key(
        String name    ) {
        this.name = name;
        this.rdbmsmm_columns = new ArrayList<>();
        this.rdbmsmm_foreignkeys = new ArrayList<>();
    }

    public rdbmsMM_Key(
        String name        ArrayList<rdbmsMM_Column> rdbmsmm_columns,        ArrayList<rdbmsMM_ForeignKey> rdbmsmm_foreignkeys    ) {
        this.name = name;
        this.rdbmsmm_columns = rdbmsmm_columns;
        this.rdbmsmm_foreignkeys = rdbmsmm_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<rdbmsMM_Column> getRdbmsmm_columns() {
        return rdbmsmm_columns;
    }

    public void addRdbmsmm_column(Rdbmsmm_column rdbmsmm_column) {
        this.rdbmsmm_columns.add(rdbmsmm_column);
    }
    public List<rdbmsMM_ForeignKey> getRdbmsmm_foreignkeys() {
        return rdbmsmm_foreignkeys;
    }

    public void addRdbmsmm_foreignkey(Rdbmsmm_foreignkey rdbmsmm_foreignkey) {
        this.rdbmsmm_foreignkeys.add(rdbmsmm_foreignkey);
    }
    public rdbmsMM_ForeignKey getRdbmsmm_foreignkey() {
        return rdbmsmm_foreignkey;
    }

    public void setRdbmsmm_foreignkey(rdbmsMM_ForeignKey rdbmsmm_foreignkey) {
        this.rdbmsmm_foreignkey = rdbmsmm_foreignkey;
    }
    public rdbmsMM_Column getRdbmsmm_column() {
        return rdbmsmm_column;
    }

    public void setRdbmsmm_column(rdbmsMM_Column rdbmsmm_column) {
        this.rdbmsmm_column = rdbmsmm_column;
    }
    public rdbmsMM_Table getRdbmsmm_table() {
        return rdbmsmm_table;
    }

    public void setRdbmsmm_table(rdbmsMM_Table rdbmsmm_table) {
        this.rdbmsmm_table = rdbmsmm_table;
    }
    public rdbmsMM_Table getRdbmsmm_table() {
        return rdbmsmm_table;
    }

    public void setRdbmsmm_table(rdbmsMM_Table rdbmsmm_table) {
        this.rdbmsmm_table = rdbmsmm_table;
    }

}