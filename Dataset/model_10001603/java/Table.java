





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String Status;
    private int Table_id;
    private int Table_num;



    public Table(
        String Status,        int Table_id,        int Table_num    ) {
        this.Status = Status;
        this.Table_id = Table_id;
        this.Table_num = Table_num;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public int getTable_id() {
        return Table_id;
    }

    public void setTable_id(int Table_id) {
        this.Table_id = Table_id;
    }
    public int getTable_num() {
        return Table_num;
    }

    public void setTable_num(int Table_num) {
        this.Table_num = Table_num;
    }


}