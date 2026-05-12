





import java.util.List;
import java.util.ArrayList;

public class Sides  {

    private boolean isVegetarian;
    private String name;
    private float price;



    public Sides(
        boolean isVegetarian,        String name,        float price    ) {
        this.isVegetarian = isVegetarian;
        this.name = name;
        this.price = price;
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
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }


}