





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String food_Id;
    private String name;
    private String description;
    private String price;
    private boolean served;
    private int type;
    private boolean prepared;





    private List<Order> orders;


    public Food(
        String food_Id,        String name,        String description,        String price,        boolean served,        int type,        boolean prepared    ) {
        this.food_Id = food_Id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.served = served;
        this.type = type;
        this.prepared = prepared;
        this.orders = new ArrayList<>();
    }

    public Food(
        String food_Id,        String name,        String description,        String price,        boolean served,        int type,        boolean prepared        ArrayList<Order> orders    ) {
        this.food_Id = food_Id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.served = served;
        this.type = type;
        this.prepared = prepared;
        this.orders = orders;
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
    public boolean getServed() {
        return served;
    }

    public void setServed(boolean served) {
        this.served = served;
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

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}