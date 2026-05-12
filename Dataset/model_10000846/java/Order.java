





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int orderSirealNumber;





    private Costomer costomer;


    public Order(
        int orderSirealNumber    ) {
        this.orderSirealNumber = orderSirealNumber;
    }


    public int getOrdersirealnumber() {
        return orderSirealNumber;
    }

    public void setOrdersirealnumber(int orderSirealNumber) {
        this.orderSirealNumber = orderSirealNumber;
    }

    public Costomer getCostomer() {
        return costomer;
    }

    public void setCostomer(Costomer costomer) {
        this.costomer = costomer;
    }

}