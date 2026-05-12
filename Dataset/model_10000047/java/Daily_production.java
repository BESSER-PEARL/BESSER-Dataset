





import java.util.List;
import java.util.ArrayList;

public class Daily_production  {

    private int future_Qty;
    private String date;
    private String pro_number;
    private int curr_qty;
    private int section;
    private String item_name;
    private String item_code;



    public Daily_production(
        int future_Qty,        String date,        String pro_number,        int curr_qty,        int section,        String item_name,        String item_code    ) {
        this.future_Qty = future_Qty;
        this.date = date;
        this.pro_number = pro_number;
        this.curr_qty = curr_qty;
        this.section = section;
        this.item_name = item_name;
        this.item_code = item_code;
    }


    public int getFuture_qty() {
        return future_Qty;
    }

    public void setFuture_qty(int future_Qty) {
        this.future_Qty = future_Qty;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getPro_number() {
        return pro_number;
    }

    public void setPro_number(String pro_number) {
        this.pro_number = pro_number;
    }
    public int getCurr_qty() {
        return curr_qty;
    }

    public void setCurr_qty(int curr_qty) {
        this.curr_qty = curr_qty;
    }
    public int getSection() {
        return section;
    }

    public void setSection(int section) {
        this.section = section;
    }
    public String getItem_name() {
        return item_name;
    }

    public void setItem_name(String item_name) {
        this.item_name = item_name;
    }
    public String getItem_code() {
        return item_code;
    }

    public void setItem_code(String item_code) {
        this.item_code = item_code;
    }


}