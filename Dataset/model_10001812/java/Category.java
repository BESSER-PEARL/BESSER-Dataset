





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String description;
    private int departmentId;
    private String categoryName;
    private int categoryID;



    public Category(
        String description,        int departmentId,        String categoryName,        int categoryID    ) {
        this.description = description;
        this.departmentId = departmentId;
        this.categoryName = categoryName;
        this.categoryID = categoryID;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getDepartmentid() {
        return departmentId;
    }

    public void setDepartmentid(int departmentId) {
        this.departmentId = departmentId;
    }
    public String getCategoryname() {
        return categoryName;
    }

    public void setCategoryname(String categoryName) {
        this.categoryName = categoryName;
    }
    public int getCategoryid() {
        return categoryID;
    }

    public void setCategoryid(int categoryID) {
        this.categoryID = categoryID;
    }


}