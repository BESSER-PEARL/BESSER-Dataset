





import java.util.List;
import java.util.ArrayList;

public class Produse  {

    private String description;
    private String name;





    private List<LineItem> lineitems;


    public Produse(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.lineitems = new ArrayList<>();
    }

    public Produse(
        String description,        String name        ArrayList<LineItem> lineitems    ) {
        this.description = description;
        this.name = name;
        this.lineitems = lineitems;
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

    public List<LineItem> getLineitems() {
        return lineitems;
    }

    public void addLineitem(Lineitem lineitem) {
        this.lineitems.add(lineitem);
    }

}