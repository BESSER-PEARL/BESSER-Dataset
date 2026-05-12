





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private int type;
    private String name;
    private boolean served;
    private String description;
    private String price;
    private boolean prepared;
    private String food_Id;





    private List<Order> orders;


    public Food(
        int type,        String name,        boolean served,        String description,        String price,        boolean prepared,        String food_Id    ) {
        this.type = type;
        this.name = name;
        this.served = served;
        this.description = description;
        this.price = price;
        this.prepared = prepared;
        this.food_Id = food_Id;
        this.orders = new ArrayList<>();
    }

    public Food(
        int type,        String name,        boolean served,        String description,        String price,        boolean prepared,        String food_Id        ArrayList<Order> orders    ) {
        this.type = type;
        this.name = name;
        this.served = served;
        this.description = description;
        this.price = price;
        this.prepared = prepared;
        this.food_Id = food_Id;
        this.orders = orders;
    }

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
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

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}