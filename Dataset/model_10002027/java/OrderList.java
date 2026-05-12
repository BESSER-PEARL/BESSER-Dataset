





import java.util.List;
import java.util.ArrayList;

public class OrderList  {

    private None orderList;





    private Order order;




    private Store store;


    public OrderList(
        None orderList    ) {
        this.orderList = orderList;
    }


    public None getOrderlist() {
        return orderList;
    }

    public void setOrderlist(None orderList) {
        this.orderList = orderList;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}