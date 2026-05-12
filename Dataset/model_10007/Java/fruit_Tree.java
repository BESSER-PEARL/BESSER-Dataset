





import java.util.List;
import java.util.ArrayList;

public class fruit_Tree  {

    private String name;





    private List<fruit_Fruit> fruit_fruits;


    public fruit_Tree(
        String name    ) {
        this.name = name;
        this.fruit_fruits = new ArrayList<>();
    }

    public fruit_Tree(
        String name        ArrayList<fruit_Fruit> fruit_fruits    ) {
        this.name = name;
        this.fruit_fruits = fruit_fruits;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fruit_Fruit> getFruit_fruits() {
        return fruit_fruits;
    }

    public void addFruit_fruit(Fruit_fruit fruit_fruit) {
        this.fruit_fruits.add(fruit_fruit);
    }

}