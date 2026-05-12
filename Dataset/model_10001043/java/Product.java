





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private int id;
    private String description;





    private List<Item> items;


    public Product(
        String name,        int id,        String description    ) {
        this.name = name;
        this.id = id;
        this.description = description;
        this.items = new ArrayList<>();
    }

    public Product(
        String name,        int id,        String description        ArrayList<Item> items    ) {
        this.name = name;
        this.id = id;
        this.description = description;
        this.items = items;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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