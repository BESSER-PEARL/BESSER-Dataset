





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private int id;
    private int TotalBill;





    private Order order;


    public Cart(
        int id,        int TotalBill    ) {
        this.id = id;
        this.TotalBill = TotalBill;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getTotalbill() {
        return TotalBill;
    }

    public void setTotalbill(int TotalBill) {
        this.TotalBill = TotalBill;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}