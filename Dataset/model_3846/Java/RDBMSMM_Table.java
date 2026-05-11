





import java.util.List;
import java.util.ArrayList;

public class RDBMSMM_Table  {

    private String name;





    private List<RDBMSMM_FKey> rdbmsmm_fkeys;




    private RDBMSMM_FKey rdbmsmm_fkey;


    public RDBMSMM_Table(
        String name    ) {
        this.name = name;
        this.rdbmsmm_fkeys = new ArrayList<>();
    }

    public RDBMSMM_Table(
        String name        ArrayList<RDBMSMM_FKey> rdbmsmm_fkeys    ) {
        this.name = name;
        this.rdbmsmm_fkeys = rdbmsmm_fkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<RDBMSMM_FKey> getRdbmsmm_fkeys() {
        return rdbmsmm_fkeys;
    }

    public void addRdbmsmm_fkey(Rdbmsmm_fkey rdbmsmm_fkey) {
        this.rdbmsmm_fkeys.add(rdbmsmm_fkey);
    }
    public RDBMSMM_FKey getRdbmsmm_fkey() {
        return rdbmsmm_fkey;
    }

    public void setRdbmsmm_fkey(RDBMSMM_FKey rdbmsmm_fkey) {
        this.rdbmsmm_fkey = rdbmsmm_fkey;
    }

}