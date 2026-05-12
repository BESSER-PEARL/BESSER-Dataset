





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None foodOrdered;
    private String order_Id;





    private Table table;


    public Order(
        None foodOrdered,        String order_Id    ) {
        this.foodOrdered = foodOrdered;
        this.order_Id = order_Id;
    }


    public None getFoodordered() {
        return foodOrdered;
    }

    public void setFoodordered(None foodOrdered) {
        this.foodOrdered = foodOrdered;
    }
    public String getOrder_id() {
        return order_Id;
    }

    public void setOrder_id(String order_Id) {
        this.order_Id = order_Id;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}