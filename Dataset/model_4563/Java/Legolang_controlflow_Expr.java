





import java.util.List;
import java.util.ArrayList;

public class Legolang_controlflow_Expr  {






    private List<OrderRobot> orderrobots;


    public Legolang_controlflow_Expr(
    ) {
        this.orderrobots = new ArrayList<>();
    }

    public Legolang_controlflow_Expr(
        ArrayList<OrderRobot> orderrobots    ) {
        this.orderrobots = orderrobots;
    }


    public List<OrderRobot> getOrderrobots() {
        return orderrobots;
    }

    public void addOrderrobot(Orderrobot orderrobot) {
        this.orderrobots.add(orderrobot);
    }

}