





import java.util.List;
import java.util.ArrayList;

public class MealDeal  {

    private float price;
    private String description;
    private boolean isVegetarian;
    private String name;





    private List<Sides> sidess;




    private List<Order> orders;




    private List<Pizza> pizzas;


    public MealDeal(
        float price,        String description,        boolean isVegetarian,        String name    ) {
        this.price = price;
        this.description = description;
        this.isVegetarian = isVegetarian;
        this.name = name;
        this.sidess = new ArrayList<>();
        this.orders = new ArrayList<>();
        this.pizzas = new ArrayList<>();
    }

    public MealDeal(
        float price,        String description,        boolean isVegetarian,        String name        ArrayList<Sides> sidess,        ArrayList<Order> orders,        ArrayList<Pizza> pizzas    ) {
        this.price = price;
        this.description = description;
        this.isVegetarian = isVegetarian;
        this.name = name;
        this.sidess = sidess;
        this.orders = orders;
        this.pizzas = pizzas;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getIsvegetarian() {
        return isVegetarian;
    }

    public void setIsvegetarian(boolean isVegetarian) {
        this.isVegetarian = isVegetarian;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Sides> getSidess() {
        return sidess;
    }

    public void addSides(Sides sides) {
        this.sidess.add(sides);
    }
    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }
    public List<Pizza> getPizzas() {
        return pizzas;
    }

    public void addPizza(Pizza pizza) {
        this.pizzas.add(pizza);
    }

}