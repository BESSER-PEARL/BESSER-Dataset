





import java.util.List;
import java.util.ArrayList;

public class trans_Table  {

    private String table2ID;
    private String table1ID;



    public trans_Table(
        String table2ID,        String table1ID    ) {
        this.table2ID = table2ID;
        this.table1ID = table1ID;
    }


    public String getTable2id() {
        return table2ID;
    }

    public void setTable2id(String table2ID) {
        this.table2ID = table2ID;
    }
    public String getTable1id() {
        return table1ID;
    }

    public void setTable1id(String table1ID) {
        this.table1ID = table1ID;
    }


}