





import java.util.List;
import java.util.ArrayList;

public class fruit_Fruit  {

    private String name;
    private String color;





    private List<fruit_Fruit> fruit_fruits;


    public fruit_Fruit(
        String name,        String color    ) {
        this.name = name;
        this.color = color;
        this.fruit_fruits = new ArrayList<>();
    }

    public fruit_Fruit(
        String name,        String color        ArrayList<fruit_Fruit> fruit_fruits    ) {
        this.name = name;
        this.color = color;
        this.fruit_fruits = fruit_fruits;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public List<fruit_Fruit> getFruit_fruits() {
        return fruit_fruits;
    }

    public void addFruit_fruit(Fruit_fruit fruit_fruit) {
        this.fruit_fruits.add(fruit_fruit);
    }

}