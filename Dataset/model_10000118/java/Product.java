





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private String description;
    private float defined;





    private List<LineItem> lineitems;


    public Product(
        String name,        String description,        float defined    ) {
        this.name = name;
        this.description = description;
        this.defined = defined;
        this.lineitems = new ArrayList<>();
    }

    public Product(
        String name,        String description,        float defined        ArrayList<LineItem> lineitems    ) {
        this.name = name;
        this.description = description;
        this.defined = defined;
        this.lineitems = lineitems;
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
    public float getDefined() {
        return defined;
    }

    public void setDefined(float defined) {
        this.defined = defined;
    }

    public List<LineItem> getLineitems() {
        return lineitems;
    }

    public void addLineitem(Lineitem lineitem) {
        this.lineitems.add(lineitem);
    }

}