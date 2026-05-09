





import java.util.List;
import java.util.ArrayList;

public class Classes_Inventory_Item  {

    private String id;
    private String name;
    private float expense;
    private float price;
    private String stock;



    public Classes_Inventory_Item(
        String id,        String name,        float expense,        float price,        String stock    ) {
        this.id = id;
        this.name = name;
        this.expense = expense;
        this.price = price;
        this.stock = stock;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getExpense() {
        return expense;
    }

    public void setExpense(float expense) {
        this.expense = expense;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getStock() {
        return stock;
    }

    public void setStock(String stock) {
        this.stock = stock;
    }


}