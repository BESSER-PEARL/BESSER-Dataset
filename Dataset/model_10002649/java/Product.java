





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String description;
    private int id;
    private String name;





    private List<Item> items;


    public Product(
        String description,        int id,        String name    ) {
        this.description = description;
        this.id = id;
        this.name = name;
        this.items = new ArrayList<>();
    }

    public Product(
        String description,        int id,        String name        ArrayList<Item> items    ) {
        this.description = description;
        this.id = id;
        this.name = name;
        this.items = items;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Item> getItems() {
        return items;
    }

    public void addItem(Item item) {
        this.items.add(item);
    }

}