





import java.util.List;
import java.util.ArrayList;

public class Manager1  {

    private String id;
    private String name;





    private List<Order1> order1s;




    private List<Stock1> stock1s;


    public Manager1(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
        this.order1s = new ArrayList<>();
        this.stock1s = new ArrayList<>();
    }

    public Manager1(
        String id,        String name        ArrayList<Order1> order1s,        ArrayList<Stock1> stock1s    ) {
        this.id = id;
        this.name = name;
        this.order1s = order1s;
        this.stock1s = stock1s;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Order1> getOrder1s() {
        return order1s;
    }

    public void addOrder1(Order1 order1) {
        this.order1s.add(order1);
    }
    public List<Stock1> getStock1s() {
        return stock1s;
    }

    public void addStock1(Stock1 stock1) {
        this.stock1s.add(stock1);
    }

}