





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private int type;
    private boolean served;
    private boolean prepared;
    private String food_Id;
    private String name;
    private String price;
    private String description;





    private List<Order> orders;


    public Food(
        int type,        boolean served,        boolean prepared,        String food_Id,        String name,        String price,        String description    ) {
        this.type = type;
        this.served = served;
        this.prepared = prepared;
        this.food_Id = food_Id;
        this.name = name;
        this.price = price;
        this.description = description;
        this.orders = new ArrayList<>();
    }

    public Food(
        int type,        boolean served,        boolean prepared,        String food_Id,        String name,        String price,        String description        ArrayList<Order> orders    ) {
        this.type = type;
        this.served = served;
        this.prepared = prepared;
        this.food_Id = food_Id;
        this.name = name;
        this.price = price;
        this.description = description;
        this.orders = orders;
    }

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public boolean getServed() {
        return served;
    }

    public void setServed(boolean served) {
        this.served = served;
    }
    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
    }
    public String getFood_id() {
        return food_Id;
    }

    public void setFood_id(String food_Id) {
        this.food_Id = food_Id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}