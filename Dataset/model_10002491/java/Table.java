





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private boolean avaliable;
    private int numSeats;
    private String table_id;



    public Table(
        boolean avaliable,        int numSeats,        String table_id    ) {
        this.avaliable = avaliable;
        this.numSeats = numSeats;
        this.table_id = table_id;
    }


    public boolean getAvaliable() {
        return avaliable;
    }

    public void setAvaliable(boolean avaliable) {
        this.avaliable = avaliable;
    }
    public int getNumseats() {
        return numSeats;
    }

    public void setNumseats(int numSeats) {
        this.numSeats = numSeats;
    }
    public String getTable_id() {
        return table_id;
    }

    public void setTable_id(String table_id) {
        this.table_id = table_id;
    }


}