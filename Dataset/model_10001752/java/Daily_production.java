





import java.util.List;
import java.util.ArrayList;

public class Daily_production  {

    private int section;
    private int curr_qty;
    private String date;
    private String item_code;
    private String pro_number;
    private String item_name;
    private int future_Qty;



    public Daily_production(
        int section,        int curr_qty,        String date,        String item_code,        String pro_number,        String item_name,        int future_Qty    ) {
        this.section = section;
        this.curr_qty = curr_qty;
        this.date = date;
        this.item_code = item_code;
        this.pro_number = pro_number;
        this.item_name = item_name;
        this.future_Qty = future_Qty;
    }


    public int getSection() {
        return section;
    }

    public void setSection(int section) {
        this.section = section;
    }
    public int getCurr_qty() {
        return curr_qty;
    }

    public void setCurr_qty(int curr_qty) {
        this.curr_qty = curr_qty;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getItem_code() {
        return item_code;
    }

    public void setItem_code(String item_code) {
        this.item_code = item_code;
    }
    public String getPro_number() {
        return pro_number;
    }

    public void setPro_number(String pro_number) {
        this.pro_number = pro_number;
    }
    public String getItem_name() {
        return item_name;
    }

    public void setItem_name(String item_name) {
        this.item_name = item_name;
    }
    public int getFuture_qty() {
        return future_Qty;
    }

    public void setFuture_qty(int future_Qty) {
        this.future_Qty = future_Qty;
    }


}