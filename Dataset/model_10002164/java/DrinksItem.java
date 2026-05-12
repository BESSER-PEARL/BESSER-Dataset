





import java.util.List;
import java.util.ArrayList;

public class DrinksItem  {

    private String drinkType;





    private Order order;


    public DrinksItem(
        String drinkType    ) {
        this.drinkType = drinkType;
    }


    public String getDrinktype() {
        return drinkType;
    }

    public void setDrinktype(String drinkType) {
        this.drinkType = drinkType;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}