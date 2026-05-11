





import java.util.List;
import java.util.ArrayList;

public class RDBMSMM_Column  {

    private String name;
    private String type;





    private RDBMSMM_FKey rdbmsmm_fkey;




    private RDBMSMM_Table rdbmsmm_table;




    private RDBMSMM_Table rdbmsmm_table;


    public RDBMSMM_Column(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public RDBMSMM_FKey getRdbmsmm_fkey() {
        return rdbmsmm_fkey;
    }

    public void setRdbmsmm_fkey(RDBMSMM_FKey rdbmsmm_fkey) {
        this.rdbmsmm_fkey = rdbmsmm_fkey;
    }
    public RDBMSMM_Table getRdbmsmm_table() {
        return rdbmsmm_table;
    }

    public void setRdbmsmm_table(RDBMSMM_Table rdbmsmm_table) {
        this.rdbmsmm_table = rdbmsmm_table;
    }
    public RDBMSMM_Table getRdbmsmm_table() {
        return rdbmsmm_table;
    }

    public void setRdbmsmm_table(RDBMSMM_Table rdbmsmm_table) {
        this.rdbmsmm_table = rdbmsmm_table;
    }

}