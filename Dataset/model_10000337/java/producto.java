




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class producto  {

    private String status;
    private String shipTo;
    private boolean shipped;
    private LocalDate ordered;
    private float total;
    private int number;





    private cliente cliente;


    public producto(
        String status,        String shipTo,        boolean shipped,        LocalDate ordered,        float total,        int number    ) {
        this.status = status;
        this.shipTo = shipTo;
        this.shipped = shipped;
        this.ordered = ordered;
        this.total = total;
        this.number = number;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
        this.shipTo = shipTo;
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

    public cliente getCliente() {
        return cliente;
    }

    public void setCliente(cliente cliente) {
        this.cliente = cliente;
    }

}