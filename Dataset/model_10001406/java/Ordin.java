




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Ordin  {

    private None status;
    private float total;
    private String shipTo;
    private int number;
    private boolean shipped;
    private LocalDate ordered;





    private Plata plata;




    private cont cont;


    public Ordin(
        None status,        float total,        String shipTo,        int number,        boolean shipped,        LocalDate ordered    ) {
        this.status = status;
        this.total = total;
        this.shipTo = shipTo;
        this.number = number;
        this.shipped = shipped;
        this.ordered = ordered;
    }


    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
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
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
    }
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
    }

    public Plata getPlata() {
        return plata;
    }

    public void setPlata(Plata plata) {
        this.plata = plata;
    }
    public cont getCont() {
        return cont;
    }

    public void setCont(cont cont) {
        this.cont = cont;
    }

}