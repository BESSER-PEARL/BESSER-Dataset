





import java.util.List;
import java.util.ArrayList;

public class MealDeal  {

    private boolean isVegetarian;
    private float price;
    private String description;
    private String name;





    private List<Sides> sidess;


    public MealDeal(
        boolean isVegetarian,        float price,        String description,        String name    ) {
        this.isVegetarian = isVegetarian;
        this.price = price;
        this.description = description;
        this.name = name;
        this.sidess = new ArrayList<>();
    }

    public MealDeal(
        boolean isVegetarian,        float price,        String description,        String name        ArrayList<Sides> sidess    ) {
        this.isVegetarian = isVegetarian;
        this.price = price;
        this.description = description;
        this.name = name;
        this.sidess = sidess;
    }

    public boolean getIsvegetarian() {
        return isVegetarian;
    }

    public void setIsvegetarian(boolean isVegetarian) {
        this.isVegetarian = isVegetarian;
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

}