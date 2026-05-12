




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Orden  {

    private float total;
    private int number;
    private String status;
    private LocalDate ordered;
    private boolean shipped;
    private String shipTo;





    private Cuenta cuenta;




    private Pago pago;


    public Orden(
        float total,        int number,        String status,        LocalDate ordered,        boolean shipped,        String shipTo    ) {
        this.total = total;
        this.number = number;
        this.status = status;
        this.ordered = ordered;
        this.shipped = shipped;
        this.shipTo = shipTo;
    }


    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
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
    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
        this.shipTo = shipTo;
    }

    public Cuenta getCuenta() {
        return cuenta;
    }

    public void setCuenta(Cuenta cuenta) {
        this.cuenta = cuenta;
    }
    public Pago getPago() {
        return pago;
    }

    public void setPago(Pago pago) {
        this.pago = pago;
    }

}