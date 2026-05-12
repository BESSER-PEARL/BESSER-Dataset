





import java.util.List;
import java.util.ArrayList;

public class Sale  {

    private String Date;
    private String Time;
    private boolean isComplete;





    private List<Sales_Line_Item> sales_line_items;


    public Sale(
        String Date,        String Time,        boolean isComplete    ) {
        this.Date = Date;
        this.Time = Time;
        this.isComplete = isComplete;
        this.sales_line_items = new ArrayList<>();
    }

    public Sale(
        String Date,        String Time,        boolean isComplete        ArrayList<Sales_Line_Item> sales_line_items    ) {
        this.Date = Date;
        this.Time = Time;
        this.isComplete = isComplete;
        this.sales_line_items = sales_line_items;
    }

    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }
    public boolean getIscomplete() {
        return isComplete;
    }

    public void setIscomplete(boolean isComplete) {
        this.isComplete = isComplete;
    }

    public List<Sales_Line_Item> getSales_line_items() {
        return sales_line_items;
    }

    public void addSales_line_item(Sales_line_item sales_line_item) {
        this.sales_line_items.add(sales_line_item);
    }

}