





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int OnlineShopID;
    private String Image;
    private int ProductID;
    private String ProductName;
    private String Price;
    private int CategoryID;
    private boolean isActive;
    private String Description;





    private OnlineShop onlineshop;




    private Category category;


    public Product(
        int OnlineShopID,        String Image,        int ProductID,        String ProductName,        String Price,        int CategoryID,        boolean isActive,        String Description    ) {
        this.OnlineShopID = OnlineShopID;
        this.Image = Image;
        this.ProductID = ProductID;
        this.ProductName = ProductName;
        this.Price = Price;
        this.CategoryID = CategoryID;
        this.isActive = isActive;
        this.Description = Description;
    }


    public int getOnlineshopid() {
        return OnlineShopID;
    }

    public void setOnlineshopid(int OnlineShopID) {
        this.OnlineShopID = OnlineShopID;
    }
    public String getImage() {
        return Image;
    }

    public void setImage(String Image) {
        this.Image = Image;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public String getProductname() {
        return ProductName;
    }

    public void setProductname(String ProductName) {
        this.ProductName = ProductName;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
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
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }

    public OnlineShop getOnlineshop() {
        return onlineshop;
    }

    public void setOnlineshop(OnlineShop onlineshop) {
        this.onlineshop = onlineshop;
    }
    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }

}