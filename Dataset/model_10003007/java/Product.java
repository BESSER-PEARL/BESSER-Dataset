





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String Description;
    private int CategoryId;
    private int UnitCost;
    private int ProductId;
    private String ModelName;
    private int ModelNumber;



    public Product(
        String Description,        int CategoryId,        int UnitCost,        int ProductId,        String ModelName,        int ModelNumber    ) {
        this.Description = Description;
        this.CategoryId = CategoryId;
        this.UnitCost = UnitCost;
        this.ProductId = ProductId;
        this.ModelName = ModelName;
        this.ModelNumber = ModelNumber;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public int getCategoryid() {
        return CategoryId;
    }

    public void setCategoryid(int CategoryId) {
        this.CategoryId = CategoryId;
    }
    public int getUnitcost() {
        return UnitCost;
    }

    public void setUnitcost(int UnitCost) {
        this.UnitCost = UnitCost;
    }
    public int getProductid() {
        return ProductId;
    }

    public void setProductid(int ProductId) {
        this.ProductId = ProductId;
    }
    public String getModelname() {
        return ModelName;
    }

    public void setModelname(String ModelName) {
        this.ModelName = ModelName;
    }
    public int getModelnumber() {
        return ModelNumber;
    }

    public void setModelnumber(int ModelNumber) {
        this.ModelNumber = ModelNumber;
    }


}