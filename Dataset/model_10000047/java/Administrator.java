





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String password;
    private String username;





    private List<Orders> orderss;


    public Administrator(
        String password,        String username    ) {
        this.password = password;
        this.username = username;
        this.orderss = new ArrayList<>();
    }

    public Administrator(
        String password,        String username        ArrayList<Orders> orderss    ) {
        this.password = password;
        this.username = username;
        this.orderss = orderss;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public List<Orders> getOrderss() {
        return orderss;
    }

    public void addOrders(Orders orders) {
        this.orderss.add(orders);
    }

}