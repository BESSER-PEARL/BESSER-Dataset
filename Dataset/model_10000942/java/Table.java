





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private int Occupied;
    private int TableNo;



    public Table(
        int Occupied,        int TableNo    ) {
        this.Occupied = Occupied;
        this.TableNo = TableNo;
    }


    public int getOccupied() {
        return Occupied;
    }

    public void setOccupied(int Occupied) {
        this.Occupied = Occupied;
    }
    public int getTableno() {
        return TableNo;
    }

    public void setTableno(int TableNo) {
        this.TableNo = TableNo;
    }


}