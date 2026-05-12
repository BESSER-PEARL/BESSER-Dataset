





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String price;
    private String name;
    private boolean served;
    private boolean prepared;
    private int type;
    private String description;
    private String food_Id;





    private List<Order> orders;


    public Food(
        String price,        String name,        boolean served,        boolean prepared,        int type,        String description,        String food_Id    ) {
        this.price = price;
        this.name = name;
        this.served = served;
        this.prepared = prepared;
        this.type = type;
        this.description = description;
        this.food_Id = food_Id;
        this.orders = new ArrayList<>();
    }

    public Food(
        String price,        String name,        boolean served,        boolean prepared,        int type,        String description,        String food_Id        ArrayList<Order> orders    ) {
        this.price = price;
        this.name = name;
        this.served = served;
        this.prepared = prepared;
        this.type = type;
        this.description = description;
        this.food_Id = food_Id;
        this.orders = orders;
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFood_id() {
        return food_Id;
    }

    public void setFood_id(String food_Id) {
        this.food_Id = food_Id;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}