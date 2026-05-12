





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int id;
    private String name;
    private String description;





    private List<Item> items;


    public Product(
        int id,        String name,        String description    ) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.items = new ArrayList<>();
    }

    public Product(
        int id,        String name,        String description        ArrayList<Item> items    ) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.items = items;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Item> getItems() {
        return items;
    }

    public void addItem(Item item) {
        this.items.add(item);
    }

}