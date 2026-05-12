





import java.util.List;
import java.util.ArrayList;

public class Meals  {

    private String MealType;
    private String unitPrice;
    private String supplier;
    private String MealID;
    private String Portion;
    private String MealName;



    public Meals(
        String MealType,        String unitPrice,        String supplier,        String MealID,        String Portion,        String MealName    ) {
        this.MealType = MealType;
        this.unitPrice = unitPrice;
        this.supplier = supplier;
        this.MealID = MealID;
        this.Portion = Portion;
        this.MealName = MealName;
    }


    public String getMealtype() {
        return MealType;
    }

    public void setMealtype(String MealType) {
        this.MealType = MealType;
    }
    public String getUnitprice() {
        return unitPrice;
    }

    public void setUnitprice(String unitPrice) {
        this.unitPrice = unitPrice;
    }
    public String getSupplier() {
        return supplier;
    }

    public void setSupplier(String supplier) {
        this.supplier = supplier;
    }
    public String getMealid() {
        return MealID;
    }

    public void setMealid(String MealID) {
        this.MealID = MealID;
    }
    public String getPortion() {
        return Portion;
    }

    public void setPortion(String Portion) {
        this.Portion = Portion;
    }
    public String getMealname() {
        return MealName;
    }

    public void setMealname(String MealName) {
        this.MealName = MealName;
    }


}