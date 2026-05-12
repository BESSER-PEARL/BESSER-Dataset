





import java.util.List;
import java.util.ArrayList;

public class Items  {

    private String re_order_qty;
    private String item_code;
    private String price_per_unit;
    private String unit_of_measure;
    private String item_id;
    private String description;





    private List<Orders> orderss;




    private List<Stock> stocks;


    public Items(
        String re_order_qty,        String item_code,        String price_per_unit,        String unit_of_measure,        String item_id,        String description    ) {
        this.re_order_qty = re_order_qty;
        this.item_code = item_code;
        this.price_per_unit = price_per_unit;
        this.unit_of_measure = unit_of_measure;
        this.item_id = item_id;
        this.description = description;
        this.orderss = new ArrayList<>();
        this.stocks = new ArrayList<>();
    }

    public Items(
        String re_order_qty,        String item_code,        String price_per_unit,        String unit_of_measure,        String item_id,        String description        ArrayList<Orders> orderss,        ArrayList<Stock> stocks    ) {
        this.re_order_qty = re_order_qty;
        this.item_code = item_code;
        this.price_per_unit = price_per_unit;
        this.unit_of_measure = unit_of_measure;
        this.item_id = item_id;
        this.description = description;
        this.orderss = orderss;
        this.stocks = stocks;
    }

    public String getRe_order_qty() {
        return re_order_qty;
    }

    public void setRe_order_qty(String re_order_qty) {
        this.re_order_qty = re_order_qty;
    }
    public String getItem_code() {
        return item_code;
    }

    public void setItem_code(String item_code) {
        this.item_code = item_code;
    }
    public String getPrice_per_unit() {
        return price_per_unit;
    }

    public void setPrice_per_unit(String price_per_unit) {
        this.price_per_unit = price_per_unit;
    }
    public String getUnit_of_measure() {
        return unit_of_measure;
    }

    public void setUnit_of_measure(String unit_of_measure) {
        this.unit_of_measure = unit_of_measure;
    }
    public String getItem_id() {
        return item_id;
    }

    public void setItem_id(String item_id) {
        this.item_id = item_id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Orders> getOrderss() {
        return orderss;
    }

    public void addOrders(Orders orders) {
        this.orderss.add(orders);
    }
    public List<Stock> getStocks() {
        return stocks;
    }

    public void addStock(Stock stock) {
        this.stocks.add(stock);
    }

}