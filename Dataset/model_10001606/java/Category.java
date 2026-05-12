





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String Name;
    private String RusName;





    private Item item;


    public Category(
        String Name,        String RusName    ) {
        this.Name = Name;
        this.RusName = RusName;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getRusname() {
        return RusName;
    }

    public void setRusname(String RusName) {
        this.RusName = RusName;
    }

    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }

}