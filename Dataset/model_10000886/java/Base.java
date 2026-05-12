





import java.util.List;
import java.util.ArrayList;

public class Base  {

    private boolean isVegetarian;
    private String name;





    private List<Pizza> pizzas;


    public Base(
        boolean isVegetarian,        String name    ) {
        this.isVegetarian = isVegetarian;
        this.name = name;
        this.pizzas = new ArrayList<>();
    }

    public Base(
        boolean isVegetarian,        String name        ArrayList<Pizza> pizzas    ) {
        this.isVegetarian = isVegetarian;
        this.name = name;
        this.pizzas = pizzas;
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

    public List<Pizza> getPizzas() {
        return pizzas;
    }

    public void addPizza(Pizza pizza) {
        this.pizzas.add(pizza);
    }

}