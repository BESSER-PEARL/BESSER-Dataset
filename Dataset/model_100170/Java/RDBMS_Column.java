





import java.util.List;
import java.util.ArrayList;

public class RDBMS_Column  {

    private String name;





    private RDBMS_Table rdbms_table;




    private RDBMS_PKey rdbms_pkey;




    private RDBMS_Table rdbms_table;




    private RDBMS_FKey rdbms_fkey;


    public RDBMS_Column(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RDBMS_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(RDBMS_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public RDBMS_PKey getRdbms_pkey() {
        return rdbms_pkey;
    }

    public void setRdbms_pkey(RDBMS_PKey rdbms_pkey) {
        this.rdbms_pkey = rdbms_pkey;
    }
    public RDBMS_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(RDBMS_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public RDBMS_FKey getRdbms_fkey() {
        return rdbms_fkey;
    }

    public void setRdbms_fkey(RDBMS_FKey rdbms_fkey) {
        this.rdbms_fkey = rdbms_fkey;
    }

}