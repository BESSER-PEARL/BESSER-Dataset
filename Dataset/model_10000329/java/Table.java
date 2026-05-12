





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String TableID;
    private int Capacity;





    private Reservation reservation;




    private Waiter waiter;


    public Table(
        String TableID,        int Capacity    ) {
        this.TableID = TableID;
        this.Capacity = Capacity;
    }


    public String getTableid() {
        return TableID;
    }

    public void setTableid(String TableID) {
        this.TableID = TableID;
    }
    public int getCapacity() {
        return Capacity;
    }

    public void setCapacity(int Capacity) {
        this.Capacity = Capacity;
    }

    public Reservation getReservation() {
        return reservation;
    }

    public void setReservation(Reservation reservation) {
        this.reservation = reservation;
    }
    public Waiter getWaiter() {
        return waiter;
    }

    public void setWaiter(Waiter waiter) {
        this.waiter = waiter;
    }

}