





import java.util.List;
import java.util.ArrayList;

public class shoppingcart  {

    private int salestax;
    private int subtotal;
    private int total;



    public shoppingcart(
        int salestax,        int subtotal,        int total    ) {
        this.salestax = salestax;
        this.subtotal = subtotal;
        this.total = total;
    }


    public int getSalestax() {
        return salestax;
    }

    public void setSalestax(int salestax) {
        this.salestax = salestax;
    }
    public int getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(int subtotal) {
        this.subtotal = subtotal;
    }
    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }


}