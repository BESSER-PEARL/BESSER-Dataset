





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private String item_id;
    private String Quantity;
    private String order_id;
    private String order_date;
    private String total_amount;
    private String status;
    private String price_per_unit;
    private String recieved_date;



    public Orders(
        String item_id,        String Quantity,        String order_id,        String order_date,        String total_amount,        String status,        String price_per_unit,        String recieved_date    ) {
        this.item_id = item_id;
        this.Quantity = Quantity;
        this.order_id = order_id;
        this.order_date = order_date;
        this.total_amount = total_amount;
        this.status = status;
        this.price_per_unit = price_per_unit;
        this.recieved_date = recieved_date;
    }


    public String getItem_id() {
        return item_id;
    }

    public void setItem_id(String item_id) {
        this.item_id = item_id;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }
    public String getOrder_id() {
        return order_id;
    }

    public void setOrder_id(String order_id) {
        this.order_id = order_id;
    }
    public String getOrder_date() {
        return order_date;
    }

    public void setOrder_date(String order_date) {
        this.order_date = order_date;
    }
    public String getTotal_amount() {
        return total_amount;
    }

    public void setTotal_amount(String total_amount) {
        this.total_amount = total_amount;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getPrice_per_unit() {
        return price_per_unit;
    }

    public void setPrice_per_unit(String price_per_unit) {
        this.price_per_unit = price_per_unit;
    }
    public String getRecieved_date() {
        return recieved_date;
    }

    public void setRecieved_date(String recieved_date) {
        this.recieved_date = recieved_date;
    }


}