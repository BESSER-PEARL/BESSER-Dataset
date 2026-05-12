





import java.util.List;
import java.util.ArrayList;

public class CompanyAddItem  {

    private String Description;
    private String Name;
    private String Price;
    private String Category;



    public CompanyAddItem(
        String Description,        String Name,        String Price,        String Category    ) {
        this.Description = Description;
        this.Name = Name;
        this.Price = Price;
        this.Category = Category;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getCategory() {
        return Category;
    }

    public void setCategory(String Category) {
        this.Category = Category;
    }


}