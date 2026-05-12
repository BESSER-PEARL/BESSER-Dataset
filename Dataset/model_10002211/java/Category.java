





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String Description;
    private String CategoryName;
    private int CategoryID;
    private boolean isActive;



    public Category(
        String Description,        String CategoryName,        int CategoryID,        boolean isActive    ) {
        this.Description = Description;
        this.CategoryName = CategoryName;
        this.CategoryID = CategoryID;
        this.isActive = isActive;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getCategoryname() {
        return CategoryName;
    }

    public void setCategoryname(String CategoryName) {
        this.CategoryName = CategoryName;
    }
    public int getCategoryid() {
        return CategoryID;
    }

    public void setCategoryid(int CategoryID) {
        this.CategoryID = CategoryID;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }


}