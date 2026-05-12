




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class MultipleChoicesAnswers  {

    private float total;
    private String shipTo;
    private int number;
    private LocalDate ordered;
    private None status;
    private boolean shipped;



    public MultipleChoicesAnswers(
        float total,        String shipTo,        int number,        LocalDate ordered,        None status,        boolean shipped    ) {
        this.total = total;
        this.shipTo = shipTo;
        this.number = number;
        this.ordered = ordered;
        this.status = status;
        this.shipped = shipped;
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
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
    }


}