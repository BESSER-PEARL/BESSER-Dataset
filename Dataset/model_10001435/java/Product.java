





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int ProductId;
    private int ModelNumber;
    private String ModelName;
    private int UnitCost;
    private int CategoryId;
    private String Description;



    public Product(
        int ProductId,        int ModelNumber,        String ModelName,        int UnitCost,        int CategoryId,        String Description    ) {
        this.ProductId = ProductId;
        this.ModelNumber = ModelNumber;
        this.ModelName = ModelName;
        this.UnitCost = UnitCost;
        this.CategoryId = CategoryId;
        this.Description = Description;
    }


    public int getProductid() {
        return ProductId;
    }

    public void setProductid(int ProductId) {
        this.ProductId = ProductId;
    }
    public int getModelnumber() {
        return ModelNumber;
    }

    public void setModelnumber(int ModelNumber) {
        this.ModelNumber = ModelNumber;
    }
    public String getModelname() {
        return ModelName;
    }

    public void setModelname(String ModelName) {
        this.ModelName = ModelName;
    }
    public int getUnitcost() {
        return UnitCost;
    }

    public void setUnitcost(int UnitCost) {
        this.UnitCost = UnitCost;
    }
    public int getCategoryid() {
        return CategoryId;
    }

    public void setCategoryid(int CategoryId) {
        this.CategoryId = CategoryId;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }


}