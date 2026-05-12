





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private int tableID;





    private Bill bill;


    public Table(
        int tableID    ) {
        this.tableID = tableID;
    }


    public int getTableid() {
        return tableID;
    }

    public void setTableid(int tableID) {
        this.tableID = tableID;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }

}