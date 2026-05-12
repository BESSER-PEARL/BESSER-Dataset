





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private String description;
    private int id;





    private List<Item> items;


    public Product(
        String name,        String description,        int id    ) {
        this.name = name;
        this.description = description;
        this.id = id;
        this.items = new ArrayList<>();
    }

    public Product(
        String name,        String description,        int id        ArrayList<Item> items    ) {
        this.name = name;
        this.description = description;
        this.id = id;
        this.items = items;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Item> getItems() {
        return items;
    }

    public void addItem(Item item) {
        this.items.add(item);
    }

}