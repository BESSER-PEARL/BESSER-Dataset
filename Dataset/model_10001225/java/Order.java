





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String foodList;
    private String order_id;



    public Order(
        String foodList,        String order_id    ) {
        this.foodList = foodList;
        this.order_id = order_id;
    }


    public String getFoodlist() {
        return foodList;
    }

    public void setFoodlist(String foodList) {
        this.foodList = foodList;
    }
    public String getOrder_id() {
        return order_id;
    }

    public void setOrder_id(String order_id) {
        this.order_id = order_id;
    }


}