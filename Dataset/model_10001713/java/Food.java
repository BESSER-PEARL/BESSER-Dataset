





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String name;
    private String price;
    private String attribute;
    private int quantity;





    private Sales_Line_Item sales_line_item;


    public Food(
        String name,        String price,        String attribute,        int quantity    ) {
        this.name = name;
        this.price = price;
        this.attribute = attribute;
        this.quantity = quantity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public Sales_Line_Item getSales_line_item() {
        return sales_line_item;
    }

    public void setSales_line_item(Sales_Line_Item sales_line_item) {
        this.sales_line_item = sales_line_item;
    }

}