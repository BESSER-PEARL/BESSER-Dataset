





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String cust_name;
    private String cust_id;
    private int numTable;
    private None foodItem;
    private String order_Id;
    private None drinksItem;



    public Order(
        String cust_name,        String cust_id,        int numTable,        None foodItem,        String order_Id,        None drinksItem    ) {
        this.cust_name = cust_name;
        this.cust_id = cust_id;
        this.numTable = numTable;
        this.foodItem = foodItem;
        this.order_Id = order_Id;
        this.drinksItem = drinksItem;
    }


    public String getCust_name() {
        return cust_name;
    }

    public void setCust_name(String cust_name) {
        this.cust_name = cust_name;
    }
    public String getCust_id() {
        return cust_id;
    }

    public void setCust_id(String cust_id) {
        this.cust_id = cust_id;
    }
    public int getNumtable() {
        return numTable;
    }

    public void setNumtable(int numTable) {
        this.numTable = numTable;
    }
    public None getFooditem() {
        return foodItem;
    }

    public void setFooditem(None foodItem) {
        this.foodItem = foodItem;
    }
    public String getOrder_id() {
        return order_Id;
    }

    public void setOrder_id(String order_Id) {
        this.order_Id = order_Id;
    }
    public None getDrinksitem() {
        return drinksItem;
    }

    public void setDrinksitem(None drinksItem) {
        this.drinksItem = drinksItem;
    }


}