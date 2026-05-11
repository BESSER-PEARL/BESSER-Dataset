





import java.util.List;
import java.util.ArrayList;

public class tables_Table  {

    private int id;
    private boolean isReserved;



    public tables_Table(
        int id,        boolean isReserved    ) {
        this.id = id;
        this.isReserved = isReserved;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getIsreserved() {
        return isReserved;
    }

    public void setIsreserved(boolean isReserved) {
        this.isReserved = isReserved;
    }


}