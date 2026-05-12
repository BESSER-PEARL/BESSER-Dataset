





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private boolean avaliable;
    private String table_id;
    private int numSeats;



    public Table(
        boolean avaliable,        String table_id,        int numSeats    ) {
        this.avaliable = avaliable;
        this.table_id = table_id;
        this.numSeats = numSeats;
    }


    public boolean getAvaliable() {
        return avaliable;
    }

    public void setAvaliable(boolean avaliable) {
        this.avaliable = avaliable;
    }
    public String getTable_id() {
        return table_id;
    }

    public void setTable_id(String table_id) {
        this.table_id = table_id;
    }
    public int getNumseats() {
        return numSeats;
    }

    public void setNumseats(int numSeats) {
        this.numSeats = numSeats;
    }


}