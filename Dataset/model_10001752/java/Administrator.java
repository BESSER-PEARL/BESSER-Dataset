





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String username;
    private String password;





    private List<Orders> orderss;


    public Administrator(
        String username,        String password    ) {
        this.username = username;
        this.password = password;
        this.orderss = new ArrayList<>();
    }

    public Administrator(
        String username,        String password        ArrayList<Orders> orderss    ) {
        this.username = username;
        this.password = password;
        this.orderss = orderss;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<Orders> getOrderss() {
        return orderss;
    }

    public void addOrders(Orders orders) {
        this.orderss.add(orders);
    }

}