





import java.util.List;
import java.util.ArrayList;

public class Licor  {

    private String description;
    private String name;





    private List<ItemOrden> itemordens;


    public Licor(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.itemordens = new ArrayList<>();
    }

    public Licor(
        String description,        String name        ArrayList<ItemOrden> itemordens    ) {
        this.description = description;
        this.name = name;
        this.itemordens = itemordens;
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

    public List<ItemOrden> getItemordens() {
        return itemordens;
    }

    public void addItemorden(Itemorden itemorden) {
        this.itemordens.add(itemorden);
    }

}