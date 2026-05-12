





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private int TableNo;
    private int Occupied;



    public Table(
        int TableNo,        int Occupied    ) {
        this.TableNo = TableNo;
        this.Occupied = Occupied;
    }


    public int getTableno() {
        return TableNo;
    }

    public void setTableno(int TableNo) {
        this.TableNo = TableNo;
    }
    public int getOccupied() {
        return Occupied;
    }

    public void setOccupied(int Occupied) {
        this.Occupied = Occupied;
    }


}