





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String name;





    private List<Stock> stocks;




    private List<Order> orders;


    public Manager(
        String name    ) {
        this.name = name;
        this.stocks = new ArrayList<>();
        this.orders = new ArrayList<>();
    }

    public Manager(
        String name        ArrayList<Stock> stocks,        ArrayList<Order> orders    ) {
        this.name = name;
        this.stocks = stocks;
        this.orders = orders;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Stock> getStocks() {
        return stocks;
    }

    public void addStock(Stock stock) {
        this.stocks.add(stock);
    }
    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}