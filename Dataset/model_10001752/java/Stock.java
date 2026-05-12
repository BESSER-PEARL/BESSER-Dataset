





import java.util.List;
import java.util.ArrayList;

public class Stock  {

    private String quantity;
    private String stock_id;
    private String item_id;
    private String exp_date;



    public Stock(
        String quantity,        String stock_id,        String item_id,        String exp_date    ) {
        this.quantity = quantity;
        this.stock_id = stock_id;
        this.item_id = item_id;
        this.exp_date = exp_date;
    }


    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getStock_id() {
        return stock_id;
    }

    public void setStock_id(String stock_id) {
        this.stock_id = stock_id;
    }
    public String getItem_id() {
        return item_id;
    }

    public void setItem_id(String item_id) {
        this.item_id = item_id;
    }
    public String getExp_date() {
        return exp_date;
    }

    public void setExp_date(String exp_date) {
        this.exp_date = exp_date;
    }


}