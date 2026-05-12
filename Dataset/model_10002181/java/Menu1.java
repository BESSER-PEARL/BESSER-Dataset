





import java.util.List;
import java.util.ArrayList;

public class Menu1  {

    private String Components;
    private String Price;
    private String Quantity;
    private String DishName;



    public Menu1(
        String Components,        String Price,        String Quantity,        String DishName    ) {
        this.Components = Components;
        this.Price = Price;
        this.Quantity = Quantity;
        this.DishName = DishName;
    }


    public String getComponents() {
        return Components;
    }

    public void setComponents(String Components) {
        this.Components = Components;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }
    public String getDishname() {
        return DishName;
    }

    public void setDishname(String DishName) {
        this.DishName = DishName;
    }


}