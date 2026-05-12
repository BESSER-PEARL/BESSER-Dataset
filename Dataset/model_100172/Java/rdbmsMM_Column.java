





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_Column  {

    private String type;
    private String name;





    private rdbmsMM_Table rdbmsmm_table;




    private rdbmsMM_ForeignKey rdbmsmm_foreignkey;




    private rdbmsMM_Table rdbmsmm_table;




    private List<rdbmsMM_ForeignKey> rdbmsmm_foreignkeys;


    public rdbmsMM_Column(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.rdbmsmm_foreignkeys = new ArrayList<>();
    }

    public rdbmsMM_Column(
        String type,        String name        ArrayList<rdbmsMM_ForeignKey> rdbmsmm_foreignkeys    ) {
        this.type = type;
        this.name = name;
        this.rdbmsmm_foreignkeys = rdbmsmm_foreignkeys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public rdbmsMM_Table getRdbmsmm_table() {
        return rdbmsmm_table;
    }

    public void setRdbmsmm_table(rdbmsMM_Table rdbmsmm_table) {
        this.rdbmsmm_table = rdbmsmm_table;
    }
    public List<rdbmsMM_ForeignKey> getRdbmsmm_foreignkeys() {
        return rdbmsmm_foreignkeys;
    }

    public void addRdbmsmm_foreignkey(Rdbmsmm_foreignkey rdbmsmm_foreignkey) {
        this.rdbmsmm_foreignkeys.add(rdbmsmm_foreignkey);
    }

}