





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int itemID;
    private String description;
    private String name;
    private String price;





    private Sales_Line_Item sales_line_item;




    private Menu menu;


    public Product(
        int itemID,        String description,        String name,        String price    ) {
        this.itemID = itemID;
        this.description = description;
        this.name = name;
        this.price = price;
    }


    public int getItemid() {
        return itemID;
    }

    public void setItemid(int itemID) {
        this.itemID = itemID;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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

    public Sales_Line_Item getSales_line_item() {
        return sales_line_item;
    }

    public void setSales_line_item(Sales_Line_Item sales_line_item) {
        this.sales_line_item = sales_line_item;
    }
    public Menu getMenu() {
        return menu;
    }

    public void setMenu(Menu menu) {
        this.menu = menu;
    }

}