




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private float total;
    private LocalDate ordered;
    private int number;
    private String status;





    private Pago pago;




    private Toma_de_pedido toma_de_pedido;


    public Order(
        float total,        LocalDate ordered,        int number,        String status    ) {
        this.total = total;
        this.ordered = ordered;
        this.number = number;
        this.status = status;
    }


    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
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

    public Pago getPago() {
        return pago;
    }

    public void setPago(Pago pago) {
        this.pago = pago;
    }
    public Toma_de_pedido getToma_de_pedido() {
        return toma_de_pedido;
    }

    public void setToma_de_pedido(Toma_de_pedido toma_de_pedido) {
        this.toma_de_pedido = toma_de_pedido;
    }

}