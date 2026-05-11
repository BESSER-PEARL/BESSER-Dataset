





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_Schema extends RModelElement {






    private rdbmsMM_Table rdbmsmm_table;




    private rdbmsMM_ForeignKey rdbmsmm_foreignkey;




    private List<rdbmsMM_Table> rdbmsmm_tables;


    public rdbmsMM_Schema(
    ) {
        super(
        );
        this.rdbmsmm_tables = new ArrayList<>();
    }

    public rdbmsMM_Schema(
        ArrayList<rdbmsMM_Table> rdbmsmm_tables    ) {
        this.rdbmsmm_tables = rdbmsmm_tables;
    }


    public rdbmsMM_Table getRdbmsmm_table() {
        return rdbmsmm_table;
    }

    public void setRdbmsmm_table(rdbmsMM_Table rdbmsmm_table) {
        this.rdbmsmm_table = rdbmsmm_table;
    }
    public rdbmsMM_ForeignKey getRdbmsmm_foreignkey() {
        return rdbmsmm_foreignkey;
    }

    public void setRdbmsmm_foreignkey(rdbmsMM_ForeignKey rdbmsmm_foreignkey) {
        this.rdbmsmm_foreignkey = rdbmsmm_foreignkey;
    }
    public List<rdbmsMM_Table> getRdbmsmm_tables() {
        return rdbmsmm_tables;
    }

    public void addRdbmsmm_table(Rdbmsmm_table rdbmsmm_table) {
        this.rdbmsmm_tables.add(rdbmsmm_table);
    }

}