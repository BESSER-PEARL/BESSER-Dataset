





import java.util.List;
import java.util.ArrayList;

public class Pizza  {

    private float price;
    private boolean isVegetarian;





    private Base base;




    private Order order;




    private List<Toppings> toppingss;




    private List<MealDeal> mealdeals;


    public Pizza(
        float price,        boolean isVegetarian    ) {
        this.price = price;
        this.isVegetarian = isVegetarian;
        this.toppingss = new ArrayList<>();
        this.mealdeals = new ArrayList<>();
    }

    public Pizza(
        float price,        boolean isVegetarian        ArrayList<Toppings> toppingss,        ArrayList<MealDeal> mealdeals    ) {
        this.price = price;
        this.isVegetarian = isVegetarian;
        this.toppingss = toppingss;
        this.mealdeals = mealdeals;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public boolean getIsvegetarian() {
        return isVegetarian;
    }

    public void setIsvegetarian(boolean isVegetarian) {
        this.isVegetarian = isVegetarian;
    }

    public Base getBase() {
        return base;
    }

    public void setBase(Base base) {
        this.base = base;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public List<Toppings> getToppingss() {
        return toppingss;
    }

    public void addToppings(Toppings toppings) {
        this.toppingss.add(toppings);
    }
    public List<MealDeal> getMealdeals() {
        return mealdeals;
    }

    public void addMealdeal(Mealdeal mealdeal) {
        this.mealdeals.add(mealdeal);
    }

}