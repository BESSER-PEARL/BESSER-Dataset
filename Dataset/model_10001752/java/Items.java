





import java.util.List;
import java.util.ArrayList;

public class Items  {

    private String item_id;
    private String unit_of_measure;
    private String re_order_qty;
    private String price_per_unit;
    private String description;
    private String item_code;





    private List<Stock> stocks;




    private List<Orders> orderss;


    public Items(
        String item_id,        String unit_of_measure,        String re_order_qty,        String price_per_unit,        String description,        String item_code    ) {
        this.item_id = item_id;
        this.unit_of_measure = unit_of_measure;
        this.re_order_qty = re_order_qty;
        this.price_per_unit = price_per_unit;
        this.description = description;
        this.item_code = item_code;
        this.stocks = new ArrayList<>();
        this.orderss = new ArrayList<>();
    }

    public Items(
        String item_id,        String unit_of_measure,        String re_order_qty,        String price_per_unit,        String description,        String item_code        ArrayList<Stock> stocks,        ArrayList<Orders> orderss    ) {
        this.item_id = item_id;
        this.unit_of_measure = unit_of_measure;
        this.re_order_qty = re_order_qty;
        this.price_per_unit = price_per_unit;
        this.description = description;
        this.item_code = item_code;
        this.stocks = stocks;
        this.orderss = orderss;
    }

    public String getItem_id() {
        return item_id;
    }

    public void setItem_id(String item_id) {
        this.item_id = item_id;
    }
    public String getUnit_of_measure() {
        return unit_of_measure;
    }

    public void setUnit_of_measure(String unit_of_measure) {
        this.unit_of_measure = unit_of_measure;
    }
    public String getRe_order_qty() {
        return re_order_qty;
    }

    public void setRe_order_qty(String re_order_qty) {
        this.re_order_qty = re_order_qty;
    }
    public String getPrice_per_unit() {
        return price_per_unit;
    }

    public void setPrice_per_unit(String price_per_unit) {
        this.price_per_unit = price_per_unit;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getItem_code() {
        return item_code;
    }

    public void setItem_code(String item_code) {
        this.item_code = item_code;
    }

    public List<Stock> getStocks() {
        return stocks;
    }

    public void addStock(Stock stock) {
        this.stocks.add(stock);
    }
    public List<Orders> getOrderss() {
        return orderss;
    }

    public void addOrders(Orders orders) {
        this.orderss.add(orders);
    }

}