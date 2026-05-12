





import java.util.List;
import java.util.ArrayList;

public class CasinoManager  {

    private None table;
    private String waitList;



    public CasinoManager(
        None table,        String waitList    ) {
        this.table = table;
        this.waitList = waitList;
    }


    public None getTable() {
        return table;
    }

    public void setTable(None table) {
        this.table = table;
    }
    public String getWaitlist() {
        return waitList;
    }

    public void setWaitlist(String waitList) {
        this.waitList = waitList;
    }


}