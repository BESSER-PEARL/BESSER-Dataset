





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String Components;
    private String DishName;
    private String Quantity;
    private String Price;



    public Menu(
        String Components,        String DishName,        String Quantity,        String Price    ) {
        this.Components = Components;
        this.DishName = DishName;
        this.Quantity = Quantity;
        this.Price = Price;
    }


    public String getComponents() {
        return Components;
    }

    public void setComponents(String Components) {
        this.Components = Components;
    }
    public String getDishname() {
        return DishName;
    }

    public void setDishname(String DishName) {
        this.DishName = DishName;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }


}