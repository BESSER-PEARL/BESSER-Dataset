





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_Schema  {

    private String name;





    private rdbmsMM_ForeignKey rdbmsmm_foreignkey;




    private List<rdbmsMM_ForeignKey> rdbmsmm_foreignkeys;


    public rdbmsMM_Schema(
        String name    ) {
        this.name = name;
        this.rdbmsmm_foreignkeys = new ArrayList<>();
    }

    public rdbmsMM_Schema(
        String name        ArrayList<rdbmsMM_ForeignKey> rdbmsmm_foreignkeys    ) {
        this.name = name;
        this.rdbmsmm_foreignkeys = rdbmsmm_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdbmsMM_ForeignKey getRdbmsmm_foreignkey() {
        return rdbmsmm_foreignkey;
    }

    public void setRdbmsmm_foreignkey(rdbmsMM_ForeignKey rdbmsmm_foreignkey) {
        this.rdbmsmm_foreignkey = rdbmsmm_foreignkey;
    }
    public List<rdbmsMM_ForeignKey> getRdbmsmm_foreignkeys() {
        return rdbmsmm_foreignkeys;
    }

    public void addRdbmsmm_foreignkey(Rdbmsmm_foreignkey rdbmsmm_foreignkey) {
        this.rdbmsmm_foreignkeys.add(rdbmsmm_foreignkey);
    }

}