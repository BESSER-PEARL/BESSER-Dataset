





import java.util.List;
import java.util.ArrayList;

public class app  {

    private String user_id;
    private String name;





    private Order order;




    private Table table;




    private Waiter waiter;


    public app(
        String user_id,        String name    ) {
        this.user_id = user_id;
        this.name = name;
    }


    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }
    public Waiter getWaiter() {
        return waiter;
    }

    public void setWaiter(Waiter waiter) {
        this.waiter = waiter;
    }

}