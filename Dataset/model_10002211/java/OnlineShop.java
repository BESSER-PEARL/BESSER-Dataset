





import java.util.List;
import java.util.ArrayList;

public class OnlineShop  {

    private int OnlineShopID;
    private boolean isActive;
    private int ShopCategoryID;
    private String OnlineShopName;





    private Category category;


    public OnlineShop(
        int OnlineShopID,        boolean isActive,        int ShopCategoryID,        String OnlineShopName    ) {
        this.OnlineShopID = OnlineShopID;
        this.isActive = isActive;
        this.ShopCategoryID = ShopCategoryID;
        this.OnlineShopName = OnlineShopName;
    }


    public int getOnlineshopid() {
        return OnlineShopID;
    }

    public void setOnlineshopid(int OnlineShopID) {
        this.OnlineShopID = OnlineShopID;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public int getShopcategoryid() {
        return ShopCategoryID;
    }

    public void setShopcategoryid(int ShopCategoryID) {
        this.ShopCategoryID = ShopCategoryID;
    }
    public String getOnlineshopname() {
        return OnlineShopName;
    }

    public void setOnlineshopname(String OnlineShopName) {
        this.OnlineShopName = OnlineShopName;
    }

    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }

}