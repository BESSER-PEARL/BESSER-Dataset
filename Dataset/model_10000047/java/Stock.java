





import java.util.List;
import java.util.ArrayList;

public class Stock  {

    private String exp_date;
    private String stock_id;
    private String quantity;
    private String item_id;



    public Stock(
        String exp_date,        String stock_id,        String quantity,        String item_id    ) {
        this.exp_date = exp_date;
        this.stock_id = stock_id;
        this.quantity = quantity;
        this.item_id = item_id;
    }


    public String getExp_date() {
        return exp_date;
    }

    public void setExp_date(String exp_date) {
        this.exp_date = exp_date;
    }
    public String getStock_id() {
        return stock_id;
    }

    public void setStock_id(String stock_id) {
        this.stock_id = stock_id;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getItem_id() {
        return item_id;
    }

    public void setItem_id(String item_id) {
        this.item_id = item_id;
    }


}