





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String description;
    private int type;
    private boolean prepared;
    private String price;
    private String name;
    private boolean served;
    private String food_Id;





    private List<Order> orders;


    public Food(
        String description,        int type,        boolean prepared,        String price,        String name,        boolean served,        String food_Id    ) {
        this.description = description;
        this.type = type;
        this.prepared = prepared;
        this.price = price;
        this.name = name;
        this.served = served;
        this.food_Id = food_Id;
        this.orders = new ArrayList<>();
    }

    public Food(
        String description,        int type,        boolean prepared,        String price,        String name,        boolean served,        String food_Id        ArrayList<Order> orders    ) {
        this.description = description;
        this.type = type;
        this.prepared = prepared;
        this.price = price;
        this.name = name;
        this.served = served;
        this.food_Id = food_Id;
        this.orders = orders;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
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