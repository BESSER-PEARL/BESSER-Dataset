





import java.util.List;
import java.util.ArrayList;

public class RDBMS_Column  {

    private String type;
    private String name;





    private RDBMS_Table rdbms_table;




    private RDBMS_Table rdbms_table;


    public RDBMS_Column(
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

    public RDBMS_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(RDBMS_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public RDBMS_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(RDBMS_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }

}