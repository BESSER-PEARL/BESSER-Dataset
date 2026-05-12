





import java.util.List;
import java.util.ArrayList;

public class Table1  {

    private String table1ID;
    private String ID;
    private String table3ID;





    private Table1 table1;


    public Table1(
        String table1ID,        String ID,        String table3ID    ) {
        this.table1ID = table1ID;
        this.ID = ID;
        this.table3ID = table3ID;
    }


    public String getTable1id() {
        return table1ID;
    }

    public void setTable1id(String table1ID) {
        this.table1ID = table1ID;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getTable3id() {
        return table3ID;
    }

    public void setTable3id(String table3ID) {
        this.table3ID = table3ID;
    }

    public Table1 getTable1() {
        return table1;
    }

    public void setTable1(Table1 table1) {
        this.table1 = table1;
    }

}