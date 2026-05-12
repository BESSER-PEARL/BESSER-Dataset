





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int Order_num;
    private int Order_id;
    private String Order_edit;
    private String Order_delete;
    private String Order_status;



    public Order(
        int Order_num,        int Order_id,        String Order_edit,        String Order_delete,        String Order_status    ) {
        this.Order_num = Order_num;
        this.Order_id = Order_id;
        this.Order_edit = Order_edit;
        this.Order_delete = Order_delete;
        this.Order_status = Order_status;
    }


    public int getOrder_num() {
        return Order_num;
    }

    public void setOrder_num(int Order_num) {
        this.Order_num = Order_num;
    }
    public int getOrder_id() {
        return Order_id;
    }

    public void setOrder_id(int Order_id) {
        this.Order_id = Order_id;
    }
    public String getOrder_edit() {
        return Order_edit;
    }

    public void setOrder_edit(String Order_edit) {
        this.Order_edit = Order_edit;
    }
    public String getOrder_delete() {
        return Order_delete;
    }

    public void setOrder_delete(String Order_delete) {
        this.Order_delete = Order_delete;
    }
    public String getOrder_status() {
        return Order_status;
    }

    public void setOrder_status(String Order_status) {
        this.Order_status = Order_status;
    }


}