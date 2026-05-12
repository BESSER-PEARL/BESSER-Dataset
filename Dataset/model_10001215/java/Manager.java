





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String name;





    private List<Order> orders;




    private List<Stock> stocks;


    public Manager(
        String name    ) {
        this.name = name;
        this.orders = new ArrayList<>();
        this.stocks = new ArrayList<>();
    }

    public Manager(
        String name        ArrayList<Order> orders,        ArrayList<Stock> stocks    ) {
        this.name = name;
        this.orders = orders;
        this.stocks = stocks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }
    public List<Stock> getStocks() {
        return stocks;
    }

    public void addStock(Stock stock) {
        this.stocks.add(stock);
    }

}