





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private int TotalBill;
    private int id;





    private Order order;


    public Cart(
        int TotalBill,        int id    ) {
        this.TotalBill = TotalBill;
        this.id = id;
    }


    public int getTotalbill() {
        return TotalBill;
    }

    public void setTotalbill(int TotalBill) {
        this.TotalBill = TotalBill;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}