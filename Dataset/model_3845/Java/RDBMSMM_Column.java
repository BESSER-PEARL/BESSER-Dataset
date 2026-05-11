





import java.util.List;
import java.util.ArrayList;

public class RDBMSMM_Column  {

    private String type;
    private String name;





    private RDBMSMM_Table rdbmsmm_table;




    private RDBMSMM_Table rdbmsmm_table;


    public RDBMSMM_Column(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
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