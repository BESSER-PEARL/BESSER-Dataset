





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private String status;
    private String order_id;
    private String price_per_unit;
    private String Quantity;
    private String total_amount;
    private String item_id;
    private String recieved_date;
    private String order_date;





    private List<Supplier> suppliers;


    public Orders(
        String status,        String order_id,        String price_per_unit,        String Quantity,        String total_amount,        String item_id,        String recieved_date,        String order_date    ) {
        this.status = status;
        this.order_id = order_id;
        this.price_per_unit = price_per_unit;
        this.Quantity = Quantity;
        this.total_amount = total_amount;
        this.item_id = item_id;
        this.recieved_date = recieved_date;
        this.order_date = order_date;
        this.suppliers = new ArrayList<>();
    }

    public Orders(
        String status,        String order_id,        String price_per_unit,        String Quantity,        String total_amount,        String item_id,        String recieved_date,        String order_date        ArrayList<Supplier> suppliers    ) {
        this.status = status;
        this.order_id = order_id;
        this.price_per_unit = price_per_unit;
        this.Quantity = Quantity;
        this.total_amount = total_amount;
        this.item_id = item_id;
        this.recieved_date = recieved_date;
        this.order_date = order_date;
        this.suppliers = suppliers;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getOrder_id() {
        return order_id;
    }

    public void setOrder_id(String order_id) {
        this.order_id = order_id;
    }
    public String getPrice_per_unit() {
        return price_per_unit;
    }

    public void setPrice_per_unit(String price_per_unit) {
        this.price_per_unit = price_per_unit;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }
    public String getTotal_amount() {
        return total_amount;
    }

    public void setTotal_amount(String total_amount) {
        this.total_amount = total_amount;
    }
    public String getItem_id() {
        return item_id;
    }

    public void setItem_id(String item_id) {
        this.item_id = item_id;
    }
    public String getRecieved_date() {
        return recieved_date;
    }

    public void setRecieved_date(String recieved_date) {
        this.recieved_date = recieved_date;
    }
    public String getOrder_date() {
        return order_date;
    }

    public void setOrder_date(String order_date) {
        this.order_date = order_date;
    }

    public List<Supplier> getSuppliers() {
        return suppliers;
    }

    public void addSupplier(Supplier supplier) {
        this.suppliers.add(supplier);
    }

}