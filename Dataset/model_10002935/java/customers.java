





import java.util.List;
import java.util.ArrayList;

public class customers  {

    private String name;
    private int shoppingCost;



    public customers(
        String name,        int shoppingCost    ) {
        this.name = name;
        this.shoppingCost = shoppingCost;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getShoppingcost() {
        return shoppingCost;
    }

    public void setShoppingcost(int shoppingCost) {
        this.shoppingCost = shoppingCost;
    }


}