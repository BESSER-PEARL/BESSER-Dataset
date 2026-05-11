





import java.util.List;
import java.util.ArrayList;

public class dDL_Column  {

    private String id;
    private int number;





    private dDL_Create_table ddl_create_table;


    public dDL_Column(
        String id,        int number    ) {
        this.id = id;
        this.number = number;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public dDL_Create_table getDdl_create_table() {
        return ddl_create_table;
    }

    public void setDdl_create_table(dDL_Create_table ddl_create_table) {
        this.ddl_create_table = ddl_create_table;
    }

}