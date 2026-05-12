




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private float total;
    private String shipTo;
    private LocalDate ordered;
    private boolean shipped;
    private int number;
    private None status;



    public Order(
        float total,        String shipTo,        LocalDate ordered,        boolean shipped,        int number,        None status    ) {
        this.total = total;
        this.shipTo = shipTo;
        this.ordered = ordered;
        this.shipped = shipped;
        this.number = number;
        this.status = status;
    }


    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
        this.shipTo = shipTo;
    }
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
    }
    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }


}