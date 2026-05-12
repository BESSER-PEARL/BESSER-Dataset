





import java.util.List;
import java.util.ArrayList;

public class SubCategory  {

    private String RusName;
    private String Name;
    private String CategoryId;





    private Item item;




    private Category category;


    public SubCategory(
        String RusName,        String Name,        String CategoryId    ) {
        this.RusName = RusName;
        this.Name = Name;
        this.CategoryId = CategoryId;
    }


    public String getRusname() {
        return RusName;
    }

    public void setRusname(String RusName) {
        this.RusName = RusName;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getCategoryid() {
        return CategoryId;
    }

    public void setCategoryid(String CategoryId) {
        this.CategoryId = CategoryId;
    }

    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }
    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }

}