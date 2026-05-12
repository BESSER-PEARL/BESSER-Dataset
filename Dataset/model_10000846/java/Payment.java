





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int Amuant;





    private Order order;


    public Payment(
        int Amuant    ) {
        this.Amuant = Amuant;
    }


    public int getAmuant() {
        return Amuant;
    }

    public void setAmuant(int Amuant) {
        this.Amuant = Amuant;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}