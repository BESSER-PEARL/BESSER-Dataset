





import java.util.List;
import java.util.ArrayList;

public class shoppingcart  {

    private int total;
    private int subtotal;
    private int salestax;



    public shoppingcart(
        int total,        int subtotal,        int salestax    ) {
        this.total = total;
        this.subtotal = subtotal;
        this.salestax = salestax;
    }


    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }
    public int getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(int subtotal) {
        this.subtotal = subtotal;
    }
    public int getSalestax() {
        return salestax;
    }

    public void setSalestax(int salestax) {
        this.salestax = salestax;
    }


}