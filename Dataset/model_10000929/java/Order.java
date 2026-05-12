





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String order_Id;
    private None foodOrdered;





    private Table table;


    public Order(
        String order_Id,        None foodOrdered    ) {
        this.order_Id = order_Id;
        this.foodOrdered = foodOrdered;
    }


    public String getOrder_id() {
        return order_Id;
    }

    public void setOrder_id(String order_Id) {
        this.order_Id = order_Id;
    }
    public None getFoodordered() {
        return foodOrdered;
    }

    public void setFoodordered(None foodOrdered) {
        this.foodOrdered = foodOrdered;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}