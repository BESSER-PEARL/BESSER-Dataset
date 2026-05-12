





import java.util.List;
import java.util.ArrayList;

public class Drink  {

    private String price;
    private int quantity;
    private String name;





    private Sales_Line_Item sales_line_item;


    public Drink(
        String price,        int quantity,        String name    ) {
        this.price = price;
        this.quantity = quantity;
        this.name = name;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Sales_Line_Item getSales_line_item() {
        return sales_line_item;
    }

    public void setSales_line_item(Sales_Line_Item sales_line_item) {
        this.sales_line_item = sales_line_item;
    }

}