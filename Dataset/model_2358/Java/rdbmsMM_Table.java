





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_Table  {

    private String name;





    private List<rdbmsMM_Column> rdbmsmm_columns;




    private rdbmsMM_Key rdbmsmm_key;




    private rdbmsMM_Schema rdbmsmm_schema;




    private rdbmsMM_Schema rdbmsmm_schema;




    private rdbmsMM_Column rdbmsmm_column;




    private rdbmsMM_Key rdbmsmm_key;




    private List<rdbmsMM_ForeignKey> rdbmsmm_foreignkeys;




    private rdbmsMM_ForeignKey rdbmsmm_foreignkey;


    public rdbmsMM_Table(
        String name    ) {
        this.name = name;
        this.rdbmsmm_columns = new ArrayList<>();
        this.rdbmsmm_foreignkeys = new ArrayList<>();
    }

    public rdbmsMM_Table(
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
    public rdbmsMM_Key getRdbmsmm_key() {
        return rdbmsmm_key;
    }

    public void setRdbmsmm_key(rdbmsMM_Key rdbmsmm_key) {
        this.rdbmsmm_key = rdbmsmm_key;
    }
    public rdbmsMM_Schema getRdbmsmm_schema() {
        return rdbmsmm_schema;
    }

    public void setRdbmsmm_schema(rdbmsMM_Schema rdbmsmm_schema) {
        this.rdbmsmm_schema = rdbmsmm_schema;
    }
    public rdbmsMM_Schema getRdbmsmm_schema() {
        return rdbmsmm_schema;
    }

    public void setRdbmsmm_schema(rdbmsMM_Schema rdbmsmm_schema) {
        this.rdbmsmm_schema = rdbmsmm_schema;
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

}